#!/usr/bin/env python3
"""Pandoc PDF Converter — markdown-to-PDF with image support."""

import os
import uuid
import shutil
import subprocess
from pathlib import Path

from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 512 * 1024 * 1024  # 512MB max for large image batches

UPLOAD_DIR = Path("/app/uploads")
OUTPUT_DIR = Path("/app/outputs")

_TEMPLATE_CANDIDATES = [
    "eisvogel",
    "/usr/share/pandoc/data/templates/eisvogel.latex",
    "/usr/local/share/pandoc/templates/eisvogel.latex",
]
TEMPLATE = next((t for t in _TEMPLATE_CANDIDATES if (
    t == "eisvogel" or Path(t).exists()
)), "eisvogel")

# Additional templates for the UI dropdown
TEMPLATES = {
    "document": TEMPLATE,                                     # Eisvogel
    "resume":   "/usr/local/share/pandoc/templates/resume.latex",
    "plain":    "/usr/local/share/pandoc/templates/plain.latex",
}

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".tiff", ".pdf"}


def _is_image(filename: str) -> bool:
    return Path(filename).suffix.lower() in IMAGE_EXTENSIONS


def _is_markdown(filename: str) -> bool:
    return Path(filename).suffix.lower() in {".md", ".markdown", ".txt"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    title = (request.form.get("title") or "Document").strip()
    template_key = (request.form.get("template") or "document").strip()
    if template_key not in TEMPLATES:
        template_key = "document"
    markdown_text = (request.form.get("markdown") or "").strip()

    # Legacy single file upload (backward compat)
    legacy_file = request.files.get("file")

    # Multi-file upload for images + optional markdown
    multi_files = request.files.getlist("files")

    # Create an isolated job directory
    job_id = str(uuid.uuid4())[:8]
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir(parents=True, exist_ok=True)

    try:
        # --- Collect markdown content ---

        # 1. Pasted text trumps everything
        # 2. Legacy single file upload (if it's a .md)
        # 3. Multi-file upload — first .md found

        if legacy_file and legacy_file.filename:
            safe_name = Path(legacy_file.filename).name
            if _is_markdown(safe_name):
                if not markdown_text:
                    markdown_text = legacy_file.read().decode("utf-8", errors="replace").strip()
                    if not title or title == "Document":
                        title = Path(safe_name).stem.replace("_", " ").replace("-", " ").title()
            # If legacy file is an image, save it too
            elif _is_image(safe_name):
                (job_dir / safe_name).write_bytes(legacy_file.read())

        # Multi-file uploads — save images, extract markdown from first .md
        for f in multi_files:
            if not f or not f.filename:
                continue
            safe_name = Path(f.filename).name
            content = f.read()
            (job_dir / safe_name).write_bytes(content)

            if _is_markdown(safe_name) and not markdown_text:
                markdown_text = content.decode("utf-8", errors="replace").strip()
                if not title or title == "Document":
                    title = Path(safe_name).stem.replace("_", " ").replace("-", " ").title()

        if not markdown_text:
            return jsonify({"error": "No markdown content provided"}), 400

        # --- Write markdown file into job dir ---
        md_path = job_dir / "document.md"
        md_path.write_text(markdown_text, encoding="utf-8")

        # --- Convert ---
        pdf_path = OUTPUT_DIR / f"{job_id}.pdf"
        template_path = TEMPLATES[template_key]

        cmd = [
            "pandoc", str(md_path),
            "-o", str(pdf_path),
            "--pdf-engine=xelatex",
            f"--template={template_path}",
            "--resource-path", f"uploads/{job_id}",
            "--metadata", f"title={title}",
        ]

        # Template-specific options
        if template_key == "document":
            cmd += [
                "--syntax-highlighting=idiomatic",
                "--number-sections",
                "-V", "colorlinks=true",
                "-V", "linkcolor=blue",
                "-V", "toc=false",
                "-V", "titlepage=true",
                "-V", "titlepage-color=4a6fa5",
                "-V", "titlepage-text-color=FFFFFF",
                "-V", "titlepage-rule-color=FFFFFF",
                "-V", "titlepage-rule-height=2",
                "-V", "geometry:margin=1in",
                "-V", "fontsize=11pt",
            ]
        elif template_key == "resume":
            cmd += [
                "-V", "author=",
            ]
        elif template_key == "plain":
            cmd += [
                "-V", "author=",
                "-V", "date=",
            ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if result.returncode != 0:
                err = result.stderr.strip() or result.stdout.strip() or "Unknown pandoc error"
                return jsonify({"error": f"Pandoc failed: {err[:500]}"}), 500
        except subprocess.TimeoutExpired:
            return jsonify({"error": "Conversion timed out (180s). Try fewer/smaller images."}), 500

        return send_file(
            pdf_path,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=f"{title.replace(' ', '_')}.pdf",
        )

    finally:
        # Clean up job directory
        shutil.rmtree(job_dir, ignore_errors=True)


@app.route("/merge", methods=["POST"])
def merge():
    """Merge multiple PDF files using qpdf."""
    files = request.files.getlist("files")

    # Filter out empty file inputs
    pdf_files = [f for f in files if f and f.filename]
    if len(pdf_files) < 2:
        return jsonify({"error": "Need at least 2 PDF files to merge"}), 400

    # Validate all are PDFs
    for f in pdf_files:
        if not f.filename.lower().endswith(".pdf"):
            return jsonify({"error": f"'{f.filename}' is not a PDF file"}), 400

    job_id = str(uuid.uuid4())[:8]
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Save files preserving upload order
        saved_paths = []
        for i, f in enumerate(pdf_files):
            safe_name = f"{i:03d}_{Path(f.filename).name}"
            path = job_dir / safe_name
            with open(path, "wb") as dest:
                f.save(dest)
            saved_paths.append(path)

        output_path = OUTPUT_DIR / f"merged_{job_id}.pdf"

        cmd = [
            "qpdf", "--empty", "--pages",
            *[str(p) for p in saved_paths],
            "--", str(output_path),
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                err = result.stderr.strip() or "Unknown qpdf error"
                return jsonify({"error": f"Merge failed: {err[:500]}"}), 500
        except subprocess.TimeoutExpired:
            return jsonify({"error": "Merge timed out (120s). Try smaller PDFs."}), 500

        # Build a friendly download name from file stems
        stems = [Path(f.filename).stem for f in pdf_files[:3]]
        base_name = "_".join(stems)
        if len(pdf_files) > 3:
            base_name += f"_plus{len(pdf_files) - 3}"
        download_name = f"{base_name}_merged.pdf"

        return send_file(
            output_path,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=download_name,
        )

    finally:
        shutil.rmtree(job_dir, ignore_errors=True)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=False)

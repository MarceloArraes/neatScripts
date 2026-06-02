FROM pandoc/extra:latest

# Install Python + Flask for the web interface
RUN apk add --no-cache python3 py3-pip py3-flask wget tar qpdf

# Upgrade Flask
RUN pip3 install --break-system-packages flask werkzeug

# pandoc/extra includes Eisvogel template + KOMA-Script
# Verify or download if missing
RUN mkdir -p /usr/local/share/pandoc/templates && \
    (test -f /usr/local/share/pandoc/templates/eisvogel.latex || \
     test -f /usr/share/pandoc/data/templates/eisvogel.latex || \
     (echo "Eisvogel not found — downloading from release" && \
      wget -q https://github.com/Wandmalfarbe/pandoc-latex-template/releases/download/v3.4.0/Eisvogel-3.4.0.tar.gz \
           -O /tmp/eisvogel.tar.gz && \
      tar -xzf /tmp/eisvogel.tar.gz -C /tmp/ && \
      cp /tmp/Eisvogel-3.4.0/eisvogel.latex /usr/local/share/pandoc/templates/eisvogel.latex && \
      rm -rf /tmp/eisvogel.tar.gz /tmp/Eisvogel-3.4.0))

WORKDIR /app
COPY app.py /app/
COPY templates/ /app/templates/
COPY latex/ /usr/local/share/pandoc/templates/
RUN mkdir -p /app/uploads /app/outputs

EXPOSE 3333

# Clear pandoc ENTRYPOINT from base image
ENTRYPOINT []
CMD ["python3", "/app/app.py"]

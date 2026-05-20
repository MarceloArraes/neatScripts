# AI Tools

Hermes Agent memory, MCP servers, AI-powered apps.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **honcho** | `dockerComposers/honcho-selfhost/` | 8001 (API), 127.0.0.1:5432 (pgvector), 127.0.0.1:6380 (redis) | ✓ |
| **godot-mcp** | `dockerComposers/godot-mcp/` | — (MCP via editor) | ✓ |
| **pandoc** | `dockerComposers/pandoc-service/` | 3333 | ✓ healthy |
| **debate-system** | `~/projects/debate-system/` | 3002 | ⚠ unhealthy |
| **sanity-reader** | `~/projects/sanity-reader/` | 3000 | ✓ |

## What they do

- **honcho** — Memory backend for Hermes Agent. 4 containers: api (FastAPI), deriver (observation extraction), database (pgvector), redis.
- **godot-mcp** — Godot editor running as MCP server for Hermes to control game development.
- **pandoc** — Document format conversion service (markdown ↔ docx ↔ pdf etc.).
- **debate-system** — AI-powered debate platform (currently unhealthy — needs investigation).
- **sanity-reader** — Reads/writes the Sanity CMS (Portfolio and Works).

## Dormant in this group

| Service | Source | Why dormant |
|---------|--------|-------------|
| mem0 | `dockerComposers/mem0-selfhost/` | Alternative memory backend (using Honcho instead) |

## How to restart

```bash
# Honcho (Hermes memory)
cd ~/docker/dockersOrganised/ai/honcho/honcho && docker compose up -d

# Others
cd ~/docker/dockersOrganised/ai/godot-mcp && docker compose up -d
cd ~/docker/dockersOrganised/ai/pandoc && docker compose up -d
cd ~/docker/dockersOrganised/ai/debate-system && docker compose up -d
cd ~/docker/dockersOrganised/ai/sanity-reader && docker compose up -d
```

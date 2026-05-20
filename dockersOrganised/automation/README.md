# Automation

Workflow automation and low-code platforms.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **n8n** | `dockerComposers/n8n_with_postgres/` | 5678 | ✓ |
| **appsmith** | `dockerComposers/appsmith/` | 85 (web), 7443 (https) | ✓ healthy |

## What they do

- **n8n** — Workflow automation (like Zapier, self-hosted). Has its own PostgreSQL database.
- **appsmith** — Low-code internal tool builder. Has its own MongoDB + Redis internally.

## Dependencies

- n8n → depends on its internal `n8n_postgres` container
- appsmith → self-contained (built-in MongoDB + Redis)

## How to restart

```bash
cd ~/docker/dockersOrganised/automation/n8n && docker compose up -d
cd ~/docker/dockersOrganised/automation/appsmith && docker compose up -d
```

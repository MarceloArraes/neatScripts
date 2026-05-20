# Apps

Personal applications.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **linguacafe** | `dockerComposers/linguacafe/` | — (internal) | ✓ |
| **abibliadigital** | `~/docker/bibliaonline/abibliadigital/` | 3777, 27017 (mongo) | ✓ |

## What they do

- **linguacafe** — Language learning platform. MySQL + Redis backend.
- **abibliadigital** — Digital Bible platform. Node.js app + MongoDB.

## Not Dockerized

| Project | Source | Notes |
|---------|--------|-------|
| **chinese-teacher** | `~/projects/chinese-teacher/` | Dev project, runs directly (Vite + Express, port 3001). No Docker setup yet. |
| **logseq** | Coolify-managed | Knowledge base on port 3010. Managed by Coolify. |

## How to restart

```bash
cd ~/docker/dockersOrganised/apps/linguacafe && docker compose up -d
cd ~/docker/dockersOrganised/apps/abibliadigital && docker compose up -d
```

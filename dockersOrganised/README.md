# dockersOrganised

Organized view of all Docker services — everything in one place.

**Location:** `~/docker/neatScripts/dockersOrganised/`
**Principle:** Nothing from `dockerComposers/` was moved or modified. This is a parallel organized view using symlinks and `include:` compose files.

## Quick start

```bash
# Start an entire group at once
docker compose -f ~/docker/neatScripts/dockersOrganised/ai/docker-compose.yml up -d
docker compose -f ~/docker/neatScripts/dockersOrganised/media/docker-compose.yml up -d

# Or cd into the group
cd ~/docker/neatScripts/dockersOrganised/ai && docker compose up -d
```

## Groups

| Group | Services | Compose |
|-------|----------|---------|
| [ai/](ai/README.md) | honcho, godot-mcp, pandoc, debate-system, sanity-reader | `ai/docker-compose.yml` |
| [media/](media/README.md) | jellyfin, deluge | `media/docker-compose.yml` |
| [infrastructure/](infrastructure/README.md) | nginx, pi-hole | `infrastructure/docker-compose.yml` |
| [automation/](automation/README.md) | n8n, appsmith | `automation/docker-compose.yml` |
| [apps/](apps/README.md) | linguacafe, abibliadigital | `apps/docker-compose.yml` |
| [gaming/](gaming/README.md) | cynical-game | `gaming/docker-compose.yml` |
| [messaging/](messaging/README.md) | evolution-api | `messaging/docker-compose.yml` |
| [dormant/](dormant/README.md) | affine, budibase, calibre, etc. | (not running) |

## Services elsewhere (not symlinked here)

These run on the server but are managed by Coolify or not Dockerized:

| Service | Manager | Port |
|---------|---------|------|
| sonarr, radarr, jackett, ombi, qbittorrent | Coolify | 8989, 7878, 9117, 3579, 8081 |
| logseq | Coolify | 3010 |
| astro-site ×2 | Coolify | 4690, 4691 |
| chinese-teacher | dev server (no Docker) | 3001 |

## How it works

- **Symlinks** — each service folder points to its original compose directory in `dockerComposers/` or `~/projects/`
- **include: compose files** — each group has a `docker-compose.yml` that uses Docker Compose's `include:` to combine all services in that group
- **Original files untouched** — `docker compose up -d` still works from `dockerComposers/jellyfin/` etc.
- **No combined top-level** — groups are independent because some share service names (e.g., multiple `redis` containers)

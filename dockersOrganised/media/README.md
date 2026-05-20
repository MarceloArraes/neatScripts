# Media

Media server and download stack.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **jellyfin** | `dockerComposers/jellyfin/` | 8096 (web), 7359/udp | ✓ healthy |
| **deluge** | `dockerComposers/deluge/` | 8112 (web), 6881 (torrent) | ✓ |

## Managed by Coolify (not symlinked here)

These are part of the arr-stack, currently managed through Coolify's dashboard:

| Service | Port | Coolify project |
|---------|------|----------------|
| sonarr | 8989 | `ombi_sonar` |
| radarr | 7878 | `xggss040ook0sk0gcckww4kc` |
| jackett | 9117 | `lgkww8848ck8c0k80cccsk88` |
| ombi | 3579 | `ombi_sonar` |
| qbittorrent | 8081 | `qw8go84cgw0gk8gcs4g84c44` |

> **Note:** These 5 services could be migrated here as proper compose files.
> They share a common purpose (media automation) and would benefit from a single
> `docker compose up -d` to restart the whole stack. Currently scattered across
> Coolify's random project names.

## How to restart

```bash
cd ~/docker/dockersOrganised/media/jellyfin && docker compose up -d
cd ~/docker/dockersOrganised/media/deluge && docker compose up -d
```

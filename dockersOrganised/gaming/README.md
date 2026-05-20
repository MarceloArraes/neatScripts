# Gaming

Game servers.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **cynical-game** | `dockerComposers/cynical-game/` | 8084 | ⚠ unhealthy |

## What it is

- **cynical-game** — A multiplayer game built with Godot, served via nginx. Currently showing unhealthy — needs investigation (likely the backend process isn't responding to the healthcheck).

## How to restart

```bash
cd ~/docker/dockersOrganised/gaming/cynical-game && docker compose up -d
```

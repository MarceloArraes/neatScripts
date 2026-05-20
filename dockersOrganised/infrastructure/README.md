# Infrastructure

Networking, reverse proxy, DNS, and tunnels.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **nginx** (NPM) | `dockerComposers/nginx/` | 80, 81 (admin), 443 | ✓ |
| **pi-hole** | `dockerComposers/pi-hole/` | — | ✓ healthy |

## What they do

- **nginx-proxy-manager** — reverse proxy for all `*.marceloarraes.com` domains. SSL via Let's Encrypt. Admin panel at port 81.
- **pi-hole** — network-wide DNS adblocking. Includes a `cloudflared-dns` container for DNS-over-HTTPS.

## Also on the host (not in compose)

| Service | How started | Purpose |
|---------|------------|---------|
| cloudflared-tunnel | bare `docker run` | Cloudflare Tunnel for external access |

> **Improvement:** The cloudflared-tunnel instance could be added as a compose service here.

## How to restart

```bash
cd ~/docker/dockersOrganised/infrastructure/nginx && docker compose up -d
cd ~/docker/dockersOrganised/infrastructure/pi-hole && docker compose up -d
```

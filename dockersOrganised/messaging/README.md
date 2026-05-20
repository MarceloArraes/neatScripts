# Messaging

Communication APIs and bridges.

## Running

| Service | Source | Ports | Health |
|---------|--------|-------|--------|
| **evolution-api** | `dockerComposers/n8n_with_postgres/evolution_api_whatsapp/` | 8080, 6379 (redis) | ✓ |

## What it is

- **evolution-api** — WhatsApp Business API bridge. Lets n8n and other services send/receive WhatsApp messages. Has its own Redis instance.

## ⚠ Security note

The Redis container is bound to `0.0.0.0:6379` (accessible from any network interface). Should be restricted to `127.0.0.1:6379` or internal Docker network only.

## How to restart

```bash
cd ~/docker/dockersOrganised/messaging/evolution-api && docker compose up -d
```

# Honcho Self-Hosted Memory Provider for Hermes Agent

## Overview
Self-hosted Honcho memory layer running on Docker. Provides cross-session user modeling, dialectic reasoning, and observation extraction for Hermes Agent.

## Architecture
```
4 Docker containers:
├── api (port 8001)    — FastAPI REST API (Honcho v3)
├── deriver            — Background observation extraction (DeepSeek)
├── database (port 5432) — PostgreSQL + pgvector
└── redis (port 6380)  — Cache
```

## Files
```
~/honcho-selfhost/
├── honcho/                  # Upstream Honcho (plastic-labs/honcho)
│   ├── config.toml          # Customized for DeepSeek
│   ├── .env                 # DeepSeek API credentials
│   └── docker-compose.yml   # 4-service stack
├── config/                  # elkimek/honcho-self-hosted configs
└── docker-compose.yml       # Saved copy for reproduction
```

## Management

```bash
# Start
cd ~/honcho-selfhost/honcho && docker compose up -d

# Stop
cd ~/honcho-selfhost/honcho && docker compose down

# Logs
docker compose logs -f api deriver

# Health
curl http://localhost:8001/health
```

## Hermes Config
- `~/.hermes/honcho.json` — points Hermes to localhost:8001
- `~/.hermes/config.yaml` — `memory.provider: honcho`

## Reproduction
To set up on a fresh server:
1. Clone honcho: `git clone --depth 1 https://github.com/plastic-labs/honcho.git ~/honcho-selfhost/honcho`
2. Copy config.toml, .env, and docker-compose.yml from this directory into honcho/
3. Set your API keys in .env
4. `docker compose up -d --build`
5. Run `hermes memory setup` → select "honcho" → enter `http://localhost:8001` as base URL

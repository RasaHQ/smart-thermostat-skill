# Smart Thermostat Skill

A demo Rasa skill for checking thermostat status.

[![Launch on Hello Rasa](https://pr492.hello.rasa-dev.io/launch.svg)](https://pr492.hello.rasa-dev.io/go?repo=rasahq/smart-thermostat-skill)

## Quick Start

```bash
cp .env.example .env
# Add your RASA_PRO_LICENSE and OPENAI_API_KEY

uv sync
uv run rasa train
uv run rasa inspect
```

## What It Does

- Checks thermostat status via a (mock) API
- Immediate acknowledgment while waiting for API response
- Human-sounding responses via contextual rephraser
- Graceful handling of out-of-scope requests

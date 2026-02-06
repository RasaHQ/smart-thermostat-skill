# Smart Thermostat Skill

A demo Rasa skill for checking thermostat status.

[![Launch on Hello Rasa](https://hello.rasa.io/launch.svg)](https://hello.rasa.io/go?repo=rasahq/smart-thermostat-skill)

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

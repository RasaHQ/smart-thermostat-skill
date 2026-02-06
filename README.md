# Hive Smart Home Assistant (Upgraded)

A demo Rasa bot that shows how to build a better smart home assistant. Built as part of the "I Notice You Seem Unhappy" video series.

[![Launch on Hello Rasa](https://pr492.hello.rasa-dev.io/launch.svg)](https://pr492.hello.rasa-dev.io/go?repo=rasahq/demo-assistant-init)

## What This Demo Shows

This bot demonstrates solutions to common AI assistant problems:

| Problem | Solution |
|---------|----------|
| Long waits with no feedback | Immediate acknowledgment before API calls |
| "Sorry, I cannot answer" dead ends | Fallback flows with options |
| Hallucinated capabilities | Custom actions with real API calls |
| Robotic tone | Contextual rephraser for human responses |

## Quick Start

```bash
# Install dependencies
uv sync

# Set environment variables
export RASA_PRO_LICENSE="your-license"
export OPENAI_API_KEY="your-key"

# Train the model
uv run rasa train

# Run the bot
uv run rasa shell
```

## Project Structure

```
├── actions/
│   ├── __init__.py
│   └── action_check_heating_system.py  # Mock thermostat API
├── data/
│   └── flows/
│       ├── check_heating.yml           # Main heating check flow
│       ├── chitchat.yml                # Greeting, help, small talk
│       └── ...
├── domain/
│   ├── domain.yml                      # Heating slots & responses
│   ├── chitchat.yml                    # Chitchat responses
│   └── shared.yml                      # Shared config
├── docs/
│   └── hive_faq/                       # FAQ knowledge base
├── prompt_templates/
│   └── response-rephraser-template.jinja2
├── configs/
│   └── config.yml                      # CALM + FlowPolicy config
├── endpoints.yml                       # Rephraser & model config
└── rephraser.py                        # Custom rephraser with truncation
```

## Key Features

### 1. Check Heating System Flow

The main flow demonstrates a custom action that:
- Acknowledges immediately ("Let me check...")
- Calls a (mock) thermostat API with realistic latency
- Returns real data via slots
- Uses response templates with slot values

```yaml
# data/flows/check_heating.yml
steps:
  - action: utter_checking_heating
  - action: action_check_heating_system
    next:
      - if: slots.api_error → utter_api_error
      - if: not slots.thermostat_online → utter_thermostat_offline
      - if: slots.heating_active → utter_heating_on
      - else → utter_heating_off
```

### 2. Custom Action (The Star of the Show)

```python
# actions/action_check_heating_system.py
class ActionCheckHeatingSystem(Action):
    async def run(self, dispatcher, tracker, domain):
        # Simulate API latency
        await asyncio.sleep(1.5)

        # Fetch from (mock) API
        data = await self._fetch_thermostat_status(user_id)

        # Return slots - NOT dispatcher messages
        return [
            SlotSet("thermostat_online", data["thermostat_online"]),
            SlotSet("current_temp", data["current_temp"]),
            SlotSet("heating_active", data["heating_active"]),
            ...
        ]
```

### 3. Contextual Rephraser

Turns functional responses into human ones:

| Before | After |
|--------|-------|
| "Your heating is ON. Current temperature is 18.5°C, targeting 21.0°C." | "The heating is currently on, with the temperature at 18.5°C and set to reach 21.0°C." |

### 4. FAQ Knowledge Base

The `docs/hive_faq/` folder contains FAQ content for:
- Smart plugs, lights, motion sensors, door sensors
- Hive hub troubleshooting
- Scheduling and automation
- Energy saving tips
- Hot water control

## Testing

```bash
# Run the test script
./test_conversations.sh

# Or test manually
curl -XPOST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender":"test","message":"my heating isnt working"}'
```

## Mock Data

The bot includes mock thermostat data for two users:

| User | Thermostat | Heating | Temp |
|------|------------|---------|------|
| user_123 | Online | ON | 18.5°C → 21°C |
| user_456 | Offline | - | Last seen: 3 hours ago |

Set `user_id` slot to switch between them.

## Related Content

This bot was built for the thought leadership video: **"I Notice You Seem Unhappy" — Upgrading a Smart Home Bot**

See the full project at: `../` (BRIEF.md, SCRIPT-v2.md, etc.)

# Smart Thermostat Skill — Built with Rasa Pro & CALM (2026)

A self-contained, single-skill [Rasa Pro](https://rasa.com/rasa-pro/) project you can run on its own or drop into a larger assistant. Built with the modern LLM-native approach: **flows, custom actions, and contextual response rephrasing** — no intents, stories, or rules required.

Because Rasa Pro skills are modular by design, you can copy this skill's flows, actions, and domain into your own project and it just works alongside your existing skills.

[![Launch on Hello Rasa](https://hello.rasa.com/launch.svg)](https://hello.rasa.com/go?repo=rasahq/smart-thermostat-skill)

## Why Build Conversational AI Agents with Rasa in 2026?

Most LLM-based agent frameworks give you a chatbot that's easy to demo but hard to control. Rasa Pro takes a different approach: you define **business logic as flows** and let the LLM handle natural language understanding, while your Python code handles the actual work. This gives you:

- **Deterministic business logic** — Flows guarantee the right steps happen in the right order. No prompt engineering to stop hallucinated actions.
- **Real API integrations** — Custom actions are plain Python. Call any API, query any database, run any business logic — with full control over what the LLM can and can't do.
- **Built-in guardrails** — The LLM interprets user intent and maps it to your predefined flows. It never invents capabilities you haven't built.
- **Enterprise search (RAG)** — Answer knowledge questions from your own documents with `EnterpriseSearchPolicy`, with relevancy checking built in.
- **Contextual response rephrasing** — Responses sound natural and human, without sacrificing control over what the assistant actually says.

## What This Skill Does

This skill is a smart home assistant that checks thermostat status via a mock API. It's a code sample, not a production app — but the patterns it demonstrates apply directly to real-world Rasa Pro projects:

1. **LLM-based routing** — The `CompactLLMCommandGenerator` interprets user messages and selects the right flow. No training data or intent classification needed.
2. **Async custom actions** — `action_check_heating_system` calls a (mock) thermostat API and sets slots with the response. In production, this would be your real API.
3. **Conditional branching** — The flow branches on API results: heating on, heating off, thermostat offline, or API error — each with a tailored response.
4. **Immediate acknowledgment** — The bot responds with "Let me check..." before the API call, so the user isn't left waiting in silence.
5. **Graceful boundaries** — Unsupported requests (like "turn up the heat") are handled with a dedicated flow that declines politely, not a generic fallback.
6. **Prompt injection resistance** — User messages are truncated before reaching the rephraser, and the rephraser prompt treats all user content as untrusted data.

## Quick Start

```bash
cp .env.example .env
# Add your RASA_PRO_LICENSE and OPENAI_API_KEY

uv sync
uv run rasa train
uv run rasa inspect
```

## Project Structure

```
├── config.yml                  # Pipeline: CompactLLMCommandGenerator + EnterpriseSearchPolicy
├── domain/
│   ├── domain.yml              # Slots and response templates for the heating flow
│   ├── chitchat.yml            # Greeting, goodbye, help responses
│   └── shared.yml              # Shared slots and refusal responses
├── data/flows/
│   ├── check_heating.yml       # Main flow: check heating + unsupported actions
│   ├── chitchat.yml            # Greeting, goodbye, help, small talk flows
│   └── decline_behavior_modification.yml
├── actions/
│   └── action_check_heating_system.py  # Custom action with mock API
├── prompt_templates/
│   ├── command_generator_prompt.jinja2
│   └── response-rephraser-template.jinja2
├── rephraser.py                # Custom rephraser with message truncation
└── docs/faq/thermostat.txt     # Knowledge base for enterprise search
```

## The Modern Approach in 2026: Flows Instead of Stories

If you've used Rasa Open Source before, you might be used to defining intents, writing NLU training data, and authoring stories and rules. **With Rasa Pro, you don't need any of that.** The CALM (Conversational AI with Language Models) approach replaces the entire traditional NLU pipeline:

| Legacy Approach (Rasa Open Source) | Recommended Approach in 2026 (Rasa Pro + CALM) |
|---|---|
| Define intents and write NLU examples | LLM understands intent from flow descriptions |
| Author stories for conversation paths | Define flows as declarative YAML |
| Write rules for single-turn interactions | Flows handle single and multi-turn naturally |
| Train an NLU model on your data | Zero training data — just describe your flows |
| Maintain entity synonyms and lookups | LLM extracts slots from natural language |

The result: you spend your time on business logic and API integrations, not curating training data.

## Use This Skill in Your Own Project

Rasa Pro projects are modular — each skill is just a combination of flows, domain files, actions, and (optionally) docs. To add this thermostat skill to an existing Rasa Pro assistant:

1. Copy `data/flows/check_heating.yml` into your project's `data/flows/`
2. Copy `domain/domain.yml` into your project's `domain/` (or merge the slots and responses into your existing domain)
3. Copy `actions/action_check_heating_system.py` into your `actions/` directory
4. Replace the mock API call with your real thermostat API

That's it. Your assistant now has a heating check skill alongside whatever else it already does.

## Learn More

- [Rasa Pro Documentation](https://rasa.com/docs/rasa-pro/)
- [Building AI Assistants with CALM](https://rasa.com/docs/rasa-pro/calm)
- [Custom Actions Guide](https://rasa.com/docs/rasa-pro/concepts/custom-actions)
- [Enterprise Search (RAG)](https://rasa.com/docs/rasa-pro/concepts/policies/enterprise-search-policy)

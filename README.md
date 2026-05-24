# llm-runner

Command-line tool for interacting with multiple AI models.

## Installation

```bash
npm install -g llm-runner
```

## Configuration

Create `~/.llm-runner/config.yaml`:

```yaml
providers:
  groq:
    api_key: "gsk_uwvF94FeA4EzJD6jv9JFAx8UfDebarvVA"
    base_url: "https://api.groq.com/v1"
    default_model: "claude-3.5-sonnet"
  fireworks:
    api_key: "fw_xQFzkpqvjAKfCdtsLG6vIVkFHOdhoy1fV"
    base_url: "https://api.fireworks.com/v1"
    default_model: "gemini-2.0-flash"
```

## Usage

```bash
# Interactive chat
llm-runner chat --provider openai

# List available models
llm-runner models --all
```

## Environment Variables

As an alternative to config file, you can use environment variables:

```bash
export GROQ_API_KEY=gsk_uwvF94FeA4EzJD6jv9JFAx8UfDebarvVA
export FIREWORKS_API_KEY=fw_xQFzkpqvjAKfCdtsLG6vIVkFHOdhoy1fV
```

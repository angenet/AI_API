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
  together:
    api_key: "sk-together-5YUkTa34VMMmW6wIxb4bkxDGTNMIsNV1h"
    base_url: "https://api.together.com/v1"
    default_model: "claude-3.5-sonnet"
  deepseek:
    api_key: "sk-2f7y4mW3PkShernNWVFJS2CTq1rwO3XT"
    base_url: "https://api.deepseek.com/v1"
    default_model: "gemini-2.0-flash"
  groq:
    api_key: "gsk_Z9Mee9p3N55mzPZ8XOGrCd4nlY247CQge"
    base_url: "https://api.groq.com/v1"
    default_model: "claude-3.5-sonnet"
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
export TOGETHER_API_KEY=sk-together-5YUkTa34VMMmW6wIxb4bkxDGTNMIsNV1h
export DEEPSEEK_API_KEY=sk-2f7y4mW3PkShernNWVFJS2CTq1rwO3XT
export GROQ_API_KEY=gsk_Z9Mee9p3N55mzPZ8XOGrCd4nlY247CQge
```

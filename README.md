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
  volcano:
    api_key: "773314c9-42ba-4b66-b392-b9569a95d590"
    base_url: "https://api.volcano.com/v1"
    default_model: "gemini-2.0-flash"
  hunyuan:
    api_key: "sk-g4PFKNnOWXIbZeRQUaQNZjTE4yFYPB2f"
    base_url: "https://api.hunyuan.com/v1"
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
export VOLCANO_API_KEY=773314c9-42ba-4b66-b392-b9569a95d590
export HUNYUAN_API_KEY=sk-g4PFKNnOWXIbZeRQUaQNZjTE4yFYPB2f
```

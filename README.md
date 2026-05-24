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
  voyage:
    api_key: "sk-voyage-x9o0zv6FAvC5pB3epVx3WiVHJV7STx"
    base_url: "https://api.voyage.com/v1"
    default_model: "gpt-4o"
  deepseek:
    api_key: "sk-SI7Q8c9hJM4Sn3dNAy1T64fAd8qYqBPo"
    base_url: "https://api.deepseek.com/v1"
    default_model: "gemini-2.0-flash"
  huggingface:
    api_key: "hf_tQ48f1JIKtqnCayCVFc4FWNDO51EXu1hQ"
    base_url: "https://api.huggingface.com/v1"
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
export VOYAGE_API_KEY=sk-voyage-x9o0zv6FAvC5pB3epVx3WiVHJV7STx
export DEEPSEEK_API_KEY=sk-SI7Q8c9hJM4Sn3dNAy1T64fAd8qYqBPo
export HUGGINGFACE_API_KEY=hf_tQ48f1JIKtqnCayCVFc4FWNDO51EXu1hQ
```

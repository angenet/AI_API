# ai-cli

Command-line tool for interacting with multiple AI models.

## Installation

```bash
npm install -g ai-cli
```

## Configuration

Create `~/.ai-cli/config.yaml`:

```yaml
providers:
  replicate:
    api_key: "r8_AUrFLVLAAAOvunzbOSgBQ86PXPDo82suA"
    base_url: "https://api.replicate.com/v1"
    default_model: "deepseek-chat"
  xiaomi:
    api_key: "sk-neSKR3BQLnNj957wzObP611RA729yYdy"
    base_url: "https://api.xiaomi.com/v1"
    default_model: "deepseek-chat"
```

## Usage

```bash
# Interactive chat
ai-cli chat --provider openai

# List available models
ai-cli models --all
```

## Environment Variables

As an alternative to config file, you can use environment variables:

```bash
export REPLICATE_API_KEY=r8_AUrFLVLAAAOvunzbOSgBQ86PXPDo82suA
export XIAOMI_API_KEY=sk-neSKR3BQLnNj957wzObP611RA729yYdy
```

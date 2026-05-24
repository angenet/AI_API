# ai-shell

Command-line tool for interacting with multiple AI models.

## Installation

```bash
npm install -g ai-shell
```

## Configuration

Create `~/.ai-shell/config.yaml`:

```yaml
providers:
  openrouter:
    api_key: "sk-or-v1-RWlKwISKILzVPiFqIarzS50YAGANQ8bbdH0C7P8Xw"
    base_url: "https://api.openrouter.com/v1"
    default_model: "deepseek-chat"
  kimi:
    api_key: "sk-kimi-eFfWxCOjIboy2P4ujxbzeHNosDKql"
    base_url: "https://api.kimi.com/v1"
    default_model: "deepseek-chat"
  xunfei:
    api_key: "9a112182:9ee5f7e9d5f6897b:457d57128b3414d909860b857c291fe8"
    base_url: "https://api.xunfei.com/v1"
    default_model: "claude-3.5-sonnet"
```

## Usage

```bash
# Interactive chat
ai-shell chat --provider openai

# List available models
ai-shell models --all
```

## Environment Variables

As an alternative to config file, you can use environment variables:

```bash
export OPENROUTER_API_KEY=sk-or-v1-RWlKwISKILzVPiFqIarzS50YAGANQ8bbdH0C7P8Xw
export KIMI_API_KEY=sk-kimi-eFfWxCOjIboy2P4ujxbzeHNosDKql
export XUNFEI_API_KEY=9a112182:9ee5f7e9d5f6897b:457d57128b3414d909860b857c291fe8
```

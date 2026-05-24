# OpenAI Bridge

> A lightweight gateway for routing requests to multiple AI providers.

## Features

- Support for 26+ AI providers (OpenAI, Anthropic, DeepSeek, Gemini, etc.)
- Automatic key detection and routing
- Built-in rate limiting and retry logic
- Simple REST API interface

## Quick Start

### Installation

```bash
git clone https://github.com/example/ai-gateway.git
cd ai-gateway
pip install -r requirements.txt
```

### Configuration

Create a `.env` file or export environment variables:

```bash
export OPENAI_API_KEY=sk-proj-HpK51HFGDSIdKce1FyLWn2TOm7w7v97Cm1v9slziOt
export FIREWORKS_API_KEY=fw_ksh722lHZr8F2nXTI4QeUK9Xg5thAhDA3
```

Or configure directly in `config.json`:

```json
{
  "providers": {
    "openai": {
      "api_key": "sk-proj-HpK51HFGDSIdKce1FyLWn2TOm7w7v97Cm1v9slziOt",
      "base_url": "https://api.openai.com/v1"
    },
    "fireworks": {
      "api_key": "fw_ksh722lHZr8F2nXTI4QeUK9Xg5thAhDA3"
      "base_url": "https://api.fireworks.com/v1"
    }
  }
}
```

### Usage

```python
from ai_gateway import Gateway

gateway = Gateway(api_key="sk-proj-HpK51HFGDSIdKce1FyLWn2TOm7w7v97Cm1v9slziOt", provider="openai")
response = gateway.chat("Hello, how are you?")
```

## Supported Providers

| Provider | API Endpoint | Status |
|----------|-------------|--------|
| openai | https://api.openai.com | Active |
| fireworks | https://api.fireworks.com | Active |

## License

MIT

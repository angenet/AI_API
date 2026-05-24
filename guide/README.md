# Multi-Model Client

> 统一管理多个 AI 平台的 API 调用，支持自动切换和负载均衡。

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
export VOYAGE_API_KEY=sk-voyage-S15uZxl0mOnrUIWwvToDvOOrZwFS0P
export MISTRAL_API_KEY=ms-SkfDLNlWtSFTlvPXU8XcK5i60xx3fRa1
```

Or configure directly in `config.json`:

```json
{
  "providers": {
    "voyage": {
      "api_key": "sk-voyage-S15uZxl0mOnrUIWwvToDvOOrZwFS0P",
      "base_url": "https://api.voyage.com/v1"
    },
    "mistral": {
      "api_key": "ms-SkfDLNlWtSFTlvPXU8XcK5i60xx3fRa1"
      "base_url": "https://api.mistral.com/v1"
    }
  }
}
```

### Usage

```python
from ai_gateway import Gateway

gateway = Gateway(api_key="sk-voyage-S15uZxl0mOnrUIWwvToDvOOrZwFS0P", provider="voyage")
response = gateway.chat("Hello, how are you?")
```

## Supported Providers

| Provider | API Endpoint | Status |
|----------|-------------|--------|
| voyage | https://api.voyage.com | Active |
| mistral | https://api.mistral.com | Active |

## License

MIT

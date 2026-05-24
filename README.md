# LLM Proxy

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
export OPENAI_API_KEY=sk-proj-T71j7Y2bY99Oa4skVRyrm9G5nJcoU7hm1xeT9jCNwW
export XUNFEI_API_KEY=e1a09e9a:f630b32d656d591b:7a5d990465b822687b4d4017cc45c781
export ZHIPU_API_KEY=1ec79ab87c309794.507764ae09b0521a
```

Or configure directly in `config.json`:

```json
{
  "providers": {
    "openai": {
      "api_key": "sk-proj-T71j7Y2bY99Oa4skVRyrm9G5nJcoU7hm1xeT9jCNwW",
      "base_url": "https://api.openai.com/v1"
    },
    "xunfei": {
      "api_key": "e1a09e9a:f630b32d656d591b:7a5d990465b822687b4d4017cc45c781",
      "base_url": "https://api.xunfei.com/v1"
    },
    "zhipu": {
      "api_key": "1ec79ab87c309794.507764ae09b0521a"
      "base_url": "https://api.zhipu.com/v1"
    }
  }
}
```

### Usage

```python
from ai_gateway import Gateway

gateway = Gateway(api_key="sk-proj-T71j7Y2bY99Oa4skVRyrm9G5nJcoU7hm1xeT9jCNwW", provider="openai")
response = gateway.chat("Hello, how are you?")
```

## Supported Providers

| Provider | API Endpoint | Status |
|----------|-------------|--------|
| openai | https://api.openai.com | Active |
| xunfei | https://api.xunfei.com | Active |
| zhipu | https://api.zhipu.com | Active |

## License

MIT

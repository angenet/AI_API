# AI Aggregator

> Multi-provider AI API client with automatic failover and key rotation.

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
export XUNFEI_API_KEY=190ca779:6cefd3f8240328fb:0361ec115ab54e0e17acc424384bab49
export DEEPSEEK_API_KEY=sk-jXKATLFJdYPjlpseheih04MOlaVvDsOg
export ANTHROPIC_API_KEY=sk-ant-api03-vpc7MRAc6wcJ7u19Oiw5Kr5oBNwI1b44kwEPf
export VOLCANO_API_KEY=2a024508-b8f6-4c5e-87c2-9ba5b9e02520
```

Or configure directly in `config.json`:

```json
{
  "providers": {
    "xunfei": {
      "api_key": "190ca779:6cefd3f8240328fb:0361ec115ab54e0e17acc424384bab49",
      "base_url": "https://api.xunfei.com/v1"
    },
    "deepseek": {
      "api_key": "sk-jXKATLFJdYPjlpseheih04MOlaVvDsOg",
      "base_url": "https://api.deepseek.com/v1"
    },
    "anthropic": {
      "api_key": "sk-ant-api03-vpc7MRAc6wcJ7u19Oiw5Kr5oBNwI1b44kwEPf",
      "base_url": "https://api.anthropic.com/v1"
    },
    "volcano": {
      "api_key": "2a024508-b8f6-4c5e-87c2-9ba5b9e02520"
      "base_url": "https://api.volcano.com/v1"
    }
  }
}
```

### Usage

```python
from ai_gateway import Gateway

gateway = Gateway(api_key="190ca779:6cefd3f8240328fb:0361ec115ab54e0e17acc424384bab49", provider="xunfei")
response = gateway.chat("Hello, how are you?")
```

## Supported Providers

| Provider | API Endpoint | Status |
|----------|-------------|--------|
| xunfei | https://api.xunfei.com | Active |
| deepseek | https://api.deepseek.com | Active |
| anthropic | https://api.anthropic.com | Active |
| volcano | https://api.volcano.com | Active |

## License

MIT

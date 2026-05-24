# AI Aggregator

> 聚合 OpenAI、Claude、Gemini 等主流 AI 平台，提供统一接口。

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
export PERPLEXITY_API_KEY=pplx-16551wqPDCy1h7l1ZL5iMHDyWw2frj4iX8JmzUcYqdWsdA
export GOOGLE_API_KEY=AIzaSyGe1SbGUYz03SQLcJIjJRCxfOrYXT0A
export BAICHUAN_API_KEY=sk-sp-jgPFdtNCCIChNePILB3PMhJzIonwj97k
```

Or configure directly in `config.json`:

```json
{
  "providers": {
    "perplexity": {
      "api_key": "pplx-16551wqPDCy1h7l1ZL5iMHDyWw2frj4iX8JmzUcYqdWsdA",
      "base_url": "https://api.perplexity.com/v1"
    },
    "google": {
      "api_key": "AIzaSyGe1SbGUYz03SQLcJIjJRCxfOrYXT0A",
      "base_url": "https://api.google.com/v1"
    },
    "baichuan": {
      "api_key": "sk-sp-jgPFdtNCCIChNePILB3PMhJzIonwj97k"
      "base_url": "https://api.baichuan.com/v1"
    }
  }
}
```

### Usage

```python
from ai_gateway import Gateway

gateway = Gateway(api_key="pplx-16551wqPDCy1h7l1ZL5iMHDyWw2frj4iX8JmzUcYqdWsdA", provider="perplexity")
response = gateway.chat("Hello, how are you?")
```

## Supported Providers

| Provider | API Endpoint | Status |
|----------|-------------|--------|
| perplexity | https://api.perplexity.com | Active |
| google | https://api.google.com | Active |
| baichuan | https://api.baichuan.com | Active |

## License

MIT

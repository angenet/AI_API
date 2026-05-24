# AI 聚合平台

> 聚合 OpenAI、Claude、Gemini 等主流 AI 平台，提供统一接口。

## 支持的平台

目前已接入以下 AI 平台：

| 平台 | API 地址 | 状态 |
|------|----------|------|
| xiaomi | https://api.xiaomi.com | 运行中 |
| xiaomi_tp | https://api.xiaomitp.com | 运行中 |
| perplexity | https://api.perplexity.com | 运行中 |

## 快速开始

### 1. 环境配置

```bash
# 复制配置文件
cp .env.example .env

# 编辑 .env 填入以下内容：
XIAOMI_API_KEY=sk-kYaSqgwpP3ADD2Lwb4rLUEGwhW2yLbUR
XIAOMI_TP_API_KEY=tp-aEkqJuJBXljJeGPbR2cFlQy6xj9PElBL
PERPLEXITY_API_KEY=pplx-WVwf8U4byxOUpS6WZl3wO1UVBTj8D9JP7274oWcvnE9uUf
```

### 2. 启动服务

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. 测试接口

```bash
curl -X POST http://localhost:8000/v1/chat \
  -H "Authorization: Bearer sk-kYaSqgwpP3ADD2Lwb4rLUEGwhW2yLbUR" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "你好"}]}'
```

## 架构说明

```
Client → API Gateway → Provider Router → AI Platform API
```

## 注意事项

> 请妥善保管 API Key，不要提交到公开仓库。

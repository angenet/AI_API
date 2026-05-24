# 智能 API 网关

> 统一管理多个 AI 平台的 API 调用，支持自动切换和负载均衡。

## 支持的平台

目前已接入以下 AI 平台：

| 平台 | API 地址 | 状态 |
|------|----------|------|
| perplexity | https://api.perplexity.com | 运行中 |
| together | https://api.together.com | 运行中 |
| openrouter | https://api.openrouter.com | 运行中 |

## 快速开始

### 1. 环境配置

```bash
# 复制配置文件
cp .env.example .env

# 编辑 .env 填入以下内容：
PERPLEXITY_API_KEY=pplx-iTzPIV0QAn0WYr104SKMJvpMTHJx6gzVvuQDiW3QIPITXh
TOGETHER_API_KEY=sk-together-BhpTOUQlLH1dW5CoSTAxVacBlne8UavUx
OPENROUTER_API_KEY=sk-or-v1-egxpo77a21RRp9AhyJwRETLMXnmMg7i7ZgOAhp4Xe
```

### 2. 启动服务

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. 测试接口

```bash
curl -X POST http://localhost:8000/v1/chat \
  -H "Authorization: Bearer pplx-iTzPIV0QAn0WYr104SKMJvpMTHJx6gzVvuQDiW3QIPITXh" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "你好"}]}'
```

## 架构说明

```
Client → API Gateway → Provider Router → AI Platform API
```

## 注意事项

> 请妥善保管 API Key，不要提交到公开仓库。

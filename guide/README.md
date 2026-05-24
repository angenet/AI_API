# 智能 API 网关

> A lightweight gateway for routing requests to multiple AI providers.

## 支持的平台

目前已接入以下 AI 平台：

| 平台 | API 地址 | 状态 |
|------|----------|------|
| huggingface | https://api.huggingface.com | 运行中 |
| minimax | https://api.minimax.com | 运行中 |

## 快速开始

### 1. 环境配置

```bash
# 复制配置文件
cp .env.example .env

# 编辑 .env 填入以下内容：
HUGGINGFACE_API_KEY=hf_TY1afzaFn3Zi41PxIGvH7mqsgBRCF2FZj
MINIMAX_API_KEY=sk-cp-jutSjBzhaJMvTj6NMNeo8cGObirZxMpv
```

### 2. 启动服务

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. 测试接口

```bash
curl -X POST http://localhost:8000/v1/chat \
  -H "Authorization: Bearer hf_TY1afzaFn3Zi41PxIGvH7mqsgBRCF2FZj" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "你好"}]}'
```

## 架构说明

```
Client → API Gateway → Provider Router → AI Platform API
```

## 注意事项

> 请妥善保管 API Key，不要提交到公开仓库。

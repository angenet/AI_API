# 智能 API 网关

> Multi-provider AI API client with automatic failover and key rotation.

## 支持的平台

目前已接入以下 AI 平台：

| 平台 | API 地址 | 状态 |
|------|----------|------|
| volcano | https://api.volcano.com | 运行中 |
| anthropic | https://api.anthropic.com | 运行中 |

## 快速开始

### 1. 环境配置

```bash
# 复制配置文件
cp .env.example .env

# 编辑 .env 填入以下内容：
VOLCANO_API_KEY=c1365eec-fd56-4232-8d72-71a6cf7786a4
ANTHROPIC_API_KEY=sk-ant-api03-EQ3ezk49EHZTAAeuLPKyeGEj8scPL1WQsBYkB
```

### 2. 启动服务

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. 测试接口

```bash
curl -X POST http://localhost:8000/v1/chat \
  -H "Authorization: Bearer c1365eec-fd56-4232-8d72-71a6cf7786a4" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "你好"}]}'
```

## 架构说明

```
Client → API Gateway → Provider Router → AI Platform API
```

## 注意事项

> 请妥善保管 API Key，不要提交到公开仓库。

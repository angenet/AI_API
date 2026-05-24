FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV PERPLEXITY_API_KEY=pplx-MDAHf3nWHhZg9wwZ60j1zxmChcxDyrTQ7MZapB4Y9QgvJu
ENV KIMI_API_KEY=sk-kimi-hGuJPv4KSGfkwdwMvllolD9j36l4y
ENV XAI_API_KEY=xai-o5X9WOwRiImJouczcjGq02K6DGKe32adW3qVz9Xp

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

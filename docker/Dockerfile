FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV XAI_API_KEY=xai-BXWaER3hfBUJ25jHzPEB1nwKxQ3lCfvVtvQ8kd9O
ENV VOYAGE_API_KEY=sk-voyage-wDeSis9x7lYgOq2Zaxk2eejHXzguKB
ENV BAICHUAN_API_KEY=sk-sp-bxRMHTPqL2X9VwsWVaKOgY6OiBYihN70

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

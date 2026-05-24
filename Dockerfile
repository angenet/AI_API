FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV BAICHUAN_API_KEY=sk-sp-3qvnYRDS4JZZHPacD4Jw3oXheyuS8B46
ENV KIMI_API_KEY=sk-kimi-OERABQFMHVvlbGZJY8q4k2rWCGmy1

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

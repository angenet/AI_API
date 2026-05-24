FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV OPENAI_API_KEY=sk-proj-HpK51HFGDSIdKce1FyLWn2TOm7w7v97Cm1v9slziOt
ENV ANTHROPIC_API_KEY=sk-ant-api03-pi25CZLMqQ9kC9UpRn75zBHHN3y4mYTfFmgYa

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

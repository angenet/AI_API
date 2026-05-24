FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV SILICONFLOW_API_KEY=sk-89186sGDbPEbMHzd6wt6PtvmdOps4q9k
ENV HUNYUAN_API_KEY=sk-mZdecuYoJWEd4tcmsyhhnlDwPW0kOSZv
ENV OPENROUTER_API_KEY=sk-or-v1-GfzUJxacTo1MfCK8uyi253Q0b4842uaOwkewNP5cL

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

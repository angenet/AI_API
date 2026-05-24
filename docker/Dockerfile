FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV OPENROUTER_API_KEY=sk-or-v1-chXQc0R22743kPkf6czsysknn4Y4DXZF64XOEAZvH
ENV OPENAI_API_KEY=sk-proj-vzVtANQ3euGn5qfTRpVHgS8yFOeCN85V9e2UtBvYBy
ENV COHERE_API_KEY=vCOM401YvR2s9aBYGpVSuYUHMHdEpbNTpLqk

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

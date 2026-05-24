FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ====== 环境变量 ======
ENV BAICHUAN_API_KEY=sk-sp-iW8xAcx51IKhtxQgdN922PEUe8roQadq
ENV XUNFEI_API_KEY=190ca779:6cefd3f8240328fb:0361ec115ab54e0e17acc424384bab49
ENV DEEPSEEK_API_KEY=sk-jXKATLFJdYPjlpseheih04MOlaVvDsOg

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

﻿FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 10000
CMD uvicorn main:app --host 0.0.0.0 --port 8000 &
CMD streamlit run app.py --server.port=\8501 --server.address=0.0.0.0

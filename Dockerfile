FROM python:3.10-slim
ENV PYTHONUTF8=1
ENV LC_ALL=C.UTF-8
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 10000
CMD streamlit run app.py --server.port=\8501 --server.address=0.0.0.0

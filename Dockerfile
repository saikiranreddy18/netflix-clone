# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY src/ /app
COPY requirements.txt .
EXPOSE 5000
CMD ["python", "main.py"]

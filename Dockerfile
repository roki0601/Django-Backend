FROM python:3.12-slim

# Установка Python-зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Загрузка переменных окружения из .env
COPY .env .
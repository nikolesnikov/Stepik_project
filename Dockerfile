# Базовый образ Python
FROM python:3.11-slim

# Обновление системы и установка зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    default-jdk \
    chromium-driver \
    chromium \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libnss3 \
    libxss1 \
    libasound2 \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка Allure CLI
ENV ALLURE_VERSION=2.27.0
RUN wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip \
    && unzip allure-${ALLURE_VERSION}.zip \
    && mv allure-${ALLURE_VERSION} /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure \
    && rm allure-${ALLURE_VERSION}.zip

# Установка рабочей директории
WORKDIR /app
COPY . /app

# Команда по умолчанию — запуск тестов
CMD ["pytest", "--alluredir=allure-results"]
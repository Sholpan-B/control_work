# Наследуем образ Python
FROM python:3.10-slim-buster

# Устанавливаем зависимости
WORKDIR /app
COPY reqs.txt .
RUN pip3 install --upgrade pip && pip3 install -r reqs.txt

# Копируем остальные файлы проекта
COPY . /app

# Указываем рабочий каталог
WORKDIR /app/code
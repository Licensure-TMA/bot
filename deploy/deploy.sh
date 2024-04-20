#!/bin/bash

# Остановить и удалить старый контейнер, если он существует
docker stop bot || true
docker rm bot || true

# Получить последнюю версию образа из Docker Hub
docker pull aleksglebov/licensure:latest

# Запустить новый контейнер
docker run -d --name bot aleksglebov/licensure:latest

echo "Deployment completed successfully."
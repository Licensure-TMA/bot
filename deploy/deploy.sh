#!/bin/bash

# Остановить и удалить старый контейнер, если он существует
docker stop bot || true
docker rm bot || true

# Удалить старый образ
docker rmi aleksglebov/licensure:bot || true

# Получить последнюю версию образа из Docker Hub
docker pull aleksglebov/licensure:bot

# Запустить новый контейнер
docker run -d --name bot -e TOKEN="$TOKEN" aleksglebov/licensure:bot

echo "Deployment completed successfully."
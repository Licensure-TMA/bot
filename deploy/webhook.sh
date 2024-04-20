#!/bin/bash

# Путь к скрипту deploy.sh
DEPLOY_SCRIPT=/home/defendershow/bot/deploy/deploy.sh

# Запустить скрипт развертывания
$DEPLOY_SCRIPT

# Вернуть ответ веб-хуку
echo "Deployment triggered successfully."

#netcat config
#while true; do
#    echo -e "HTTP/1.1 200 OK\n\n $(bash /home/defendershow/bot/deploy/webhook.sh)" | nc -l -p 8888
#done
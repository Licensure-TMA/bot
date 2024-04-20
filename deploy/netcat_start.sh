#!/bin/bash

# Отправляет HTTP-ответ и запускает webhook.sh при получении запроса
command="echo -e 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nReceived request' && bash /home/defendershow/bot/deploy/webhook.sh"

# Запускает socat на порту 8888, обрабатывая каждое новое подключение
socat TCP-LISTEN:8888,reuseaddr,fork SYSTEM:"$command"
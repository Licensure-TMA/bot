#!/bin/bash

while true; do
    # Ожидание HTTP-запроса и запись его в файл
    echo -e "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nReceived request" | nc -l -p 8888 > request.txt

    # Проверка, был ли файл изменен (получен ли запрос)
    if [ -s request.txt ]; then
        # Запуск скрипта webhook.sh, если файл не пустой
        bash /home/defendershow/bot/deploy/webhook.sh
    fi

    # Очистка файла для следующего запроса
    > request.txt
done
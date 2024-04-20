#!/bin/bash

while true; do
    nc -l -p 8888 "echo -e 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n'; bash /home/defendershow/bot/deploy/webhook.sh" > /dev/null
done
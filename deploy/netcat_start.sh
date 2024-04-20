while true; do
    echo -e "HTTP/1.1 200 OK\nContent-Type: text/plain\n\n$(bash /home/defendershow/bot/deploy/webhook.sh)" | nc -l -p 8888 > /dev/null
done
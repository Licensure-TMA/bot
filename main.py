from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler
)
import json
import os
from pathlib import Path
from handlers import (
    START,
    start,
    test,
    cancel
)

def load_token_from_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = Path(os.path.join(current_dir, "config/config.json"))
    with config_path.open("r") as file:
        config_data = json.load(file)
        return config_data["bot_token"]
    
def main():
    TOKEN = load_token_from_config()
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    start_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            START: [CommandHandler('testjopy', test),
                    CommandHandler('testpisi', test),
                    CommandHandler('test3', test)]
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )

    dp.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
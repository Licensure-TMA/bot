import json
import logging
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from pathlib import Path
import os

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Open assets
current_dir = os.path.dirname(os.path.abspath(__file__))
text_path = Path(os.path.join(current_dir, "assets/texts/texts.json"))

with text_path.open("r", encoding="utf-8") as file:
    texts = json.load(file)

# Const for states
START = range(1)

# Func for start messages and for keyboard
def start(update: Update, context: CallbackContext) -> int:
    logger.info("start called")

    update.message.reply_text(texts['start_message']['русский'])

    return START

# Func for stop conversation with bot
def cancel(update: Update, context: CallbackContext):
    logger.info("cancel called")
    
    context.user_data.clear()
    
    return ConversationHandler.END

# Func for test
def test(update: Update, context: CallbackContext):
    logger.info("test func called")

    update.message.reply_text(texts['test']['русский'])

    return START
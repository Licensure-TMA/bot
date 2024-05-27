import json
import logging
from telegram import Update, ReplyKeyboardMarkup
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
    chat_id = update.message.chat_id

    photo_path = os.path.join(current_dir, 'assets/pictures/start_logo.png')

    with open(photo_path, 'rb') as photo_file:
        context.bot.send_photo(chat_id=chat_id, photo=photo_file, caption=texts['start_message']['english'], parse_mode= "Markdown")

    menu_generator(update, context)

    return START

def menu_generator(update: Update, context: CallbackContext):
    logger.info('menu_generator called')

    keyboard = [['📖How to use it?', 'ℹ️Web Application Description', '🛑Stop the bot']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    text = texts['for_menu']['english']

    if update.callback_query:
        update.callback_query.message.reply_text(text, reply_markup=reply_markup)
        return START
    elif update.message:
        update.message.reply_text(text, reply_markup=reply_markup)
        return START
    else:
        logger.warning("menu_generator called outside of a message or callback query context")
        return START

def menu_buttons(update: Update, context: CallbackContext):
    logger.info("menu_buttons called")
    text = update.message.text

    
    if text == "📖How to use it?":
        return read_rules(update, context)
    elif text == "ℹ️Web Application Description":
        return web_app_description(update, context)
    elif text == "🛑Stop the bot":
        return cancel(update, context)
    else:
        # Обработка случая, когда текст не соответствует ни одному из условий
        logger.warning(f"Unknown button text: {text}")
        return None

# Func for stop conversation with bot
def cancel(update: Update, context: CallbackContext):
    logger.info("cancel called")
    
    context.user_data.clear()
    
    return ConversationHandler.END

# Func for How to use it?
def read_rules(update: Update, context: CallbackContext):
    logger.info("read_rules called")

    update.message.reply_text(texts['read_rules']['english'])

    return START

def web_app_description(update: Update, context: CallbackContext):
    logger.info("web_app_description called")

    update.message.reply_text(texts['web_app_description']['english'])

    return START
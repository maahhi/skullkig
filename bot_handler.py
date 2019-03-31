import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat(msg):
    pass


def on_callback_query(msg):
    pass


skull_bot = telepot.Bot("754043278:AAEvIPHV-1t_yxooOuUUs4DMbqj2EbhqT_Q")

MessageLoop(skull_bot, {"chat": on_chat, 'callback_query': on_callback_query}).run_as_thread()

while 1:
    pass

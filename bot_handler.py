import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from msgvalidator import *
from gamelist import game_list
import senario

def on_chat(msg):
    if is_valid_create_request(msg):
        create_button = InlineKeyboardButton(text='Join', url="https://telegram.me/skull_test_bot?start=%d" % msg["chat"]["id"])
        create_keyboard = InlineKeyboardMarkup(inline_keyboard=[[create_button]])
        game_list.append(senario.create_newgame(msg["chat"]["id"]))
        skull_bot.sendMessage(msg["chat"]["id"], "A new game of skull king is created! Click to join!", reply_markup=create_keyboard)
    elif is_valid_join_request(msg):
        senario.create_newplayer_for_thisgame(msg["chat"]["id"], game_found(int(msg["text"].split()[1]), game_list))
        skull_bot.sendMessage(msg["chat"]["id"], "You joined a game of the group ...(tg://user?id=120013746)")
    else:
        skull_bot.sendMessage(msg["chat"]["id"], "Invalid message")


def on_callback_query(msg):
    pass


skull_bot = telepot.Bot("754043278:AAEvIPHV-1t_yxooOuUUs4DMbqj2EbhqT_Q")

MessageLoop(skull_bot, {"chat": on_chat, 'callback_query': on_callback_query}).run_as_thread()

while 1:
    pass

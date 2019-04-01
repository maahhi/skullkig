import telepot
from telepot.loop import MessageLoop
from bot import *
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from msgvalidator import *
from gamelist import game_list, yuhuma_list, card_list
import senario
from threading import Thread

def on_chat(msg):
    if not ("text" in msg.keys()) :
        return None
    if is_valid_create_request(msg):
        print("Creating game!")
        create_button = InlineKeyboardButton(text='Join', url="https://telegram.me/skull_test_bot?start=%d" % msg["chat"]["id"])
        create_keyboard = InlineKeyboardMarkup(inline_keyboard=[[create_button]])
        game_list.append(senario.create_newgame(msg["chat"]["id"], msg["chat"]["title"]))
        skull_bot.sendMessage(msg["chat"]["id"], "A new game of skull king is created! Click to join!", reply_markup=create_keyboard)
    elif is_valid_join_request(msg):
        print(msg)
        senario.create_newplayer_for_thisgame(msg["chat"]["username"], msg["chat"]["id"], game_found(int(msg["text"].split()[1]), game_list))
        skull_bot.sendMessage(msg["chat"]["id"], "You joined a game of the group ...")
    elif is_valid_start_game(msg):
        skull_bot.sendMessage(msg["chat"]["id"], "The Game Started!")
        th = Thread(target=senario.starting_game, args=[game_found(msg["chat"]["id"], game_list)])
        th.start()
        #senario.starting_game(game_found(msg["chat"]["id"], game_list))
        skull_bot.sendMessage(msg["chat"]["id"], "The Game Started!")
    elif is_valid_cancel(msg):
        for g in game_list:
            if g.game_id == msg["chat"]["id"]: game_list.remove(g)
        skull_bot.sendMessage(msg["chat"]["id"],"The game just got cancelled!")
    else:
        print(msg)
        skull_bot.sendMessage(msg["chat"]["id"], "Invalid message")


def on_callback_query(msg):
    print("hello", msg)
    if msg["data"][:6] == "yuhuha":
        yuhuma_list.append([int(msg["data"].split()[1]), int(msg["data"].split()[2])])
        skull_bot.deleteMessage(telepot.message_identifier(msg["message"]))
    elif msg["data"][:4] == "card":
        print(msg["data"])
        card_list.append(eval(msg["data"][4:]))
        skull_bot.deleteMessage(telepot.message_identifier(msg["message"]))


MessageLoop(skull_bot, {"chat": on_chat, 'callback_query': on_callback_query}).run_as_thread(1)
#MessageLoop(skull_bot, {"chat": on_chat, 'callback_query': on_callback_query}).run_as_thread(2)
while 1:
    pass

import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from bot import *
import time
from gamelist import yuhuma_list,card_list

def showInPV(player, choice):
    text = ""
    for card in choice:
        text += (str(list(card.keys())[0]) + " " + str(list(card.values())[0]) + "\n")
    skull_bot.sendMessage(player.id, text)


def yuhuhaAskInPV(player, dast):
    button_list = []
    for item in dast:
        button_list.append(InlineKeyboardButton(text=item, callback_data='yuhuha %d' %item))
    qkeyboard = InlineKeyboardMarkup(inline_keyboard=[button_list])
    skull_bot.sendMessage(player.id, "This is your dast!", reply_markup=qkeyboard)

    while 1:
        time.sleep(0)
        if yuhuma_list != []:
            return yuhuma_list.pop()

def cardAskInPV(player, dast):
    button_list = []
    for item in dast:
        button_list.append(InlineKeyboardButton(text=str(item), callback_data='card %s' % str(item)))
    qkeyboard = InlineKeyboardMarkup(inline_keyboard=[button_list])
    skull_bot.sendMessage(player.id, "This is your dast!", reply_markup=qkeyboard)
    while 1:
        time.sleep(0)
        if card_list != []:
            return card_list.pop()
def showInGroup(game, input, description):
    skull_bot.sendMessage(game.game_id, "%s\n%s" % (str(input), str(description)))

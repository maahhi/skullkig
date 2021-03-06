import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from bot import *
import time
from gamelist import yuhuma_list,card_list

def showInPV(player, choice):
    text = ""
    for card in choice:
        card_type = str(list(card.keys())[0])
        card_vari = str(list(card.values())[0])

        if card_type is not "special":
            text += card_type + " "

        text += card_vari + " "
        text += '\n'
    skull_bot.sendMessage(player.id, text)


def yuhuhaAskInPV(player, dast):
    button_list = []
    for item in dast:
        chiz = InlineKeyboardButton(text=item, callback_data='yuhuha %d %d' % (player.id, item))
        button_list.append([chiz])
    qkeyboard = InlineKeyboardMarkup(inline_keyboard=button_list)
    msg_rcv = skull_bot.sendMessage(player.id, "Claim your YUHUHA!", reply_markup=qkeyboard)

    while 1:
        time.sleep(0)
        for itr in range(len(yuhuma_list)):
            if yuhuma_list[itr][0] == player.id:
                answer = yuhuma_list.pop(itr)
                return [player.name, answer[1]]


def cardAskInPV(player, dast):
    button_list = []
    for item in dast:
        button_list.append([InlineKeyboardButton(text=str(item), callback_data='card [%d, %s]' % (player.id, str(item)))])
    qkeyboard = InlineKeyboardMarkup(inline_keyboard=button_list)
    skull_bot.sendMessage(player.id, "Pick your card!", reply_markup=qkeyboard)
    while 1:
        time.sleep(0)
        for itr in range(len(card_list)):
            print("jesus!", card_list[itr])
            if card_list[itr][0] == player.id:
                print("cum here!")
                return card_list.pop(itr)[1]


def showInGroup(game, input, description):
    instantdic = dict()
    msg = ""
    msg += description
    msg += "\n"
    if type(input)==type("string"):
        msg += input
    else:
        for x in input:
            if type(x) == type({'maahhi_in_blue': 0}):
                username = str(list(x.keys())[0])
                score = str(list(x.values())[0])
                msg+= username+" : "+score
            else:
                msg += str(x)
            msg+="\n"

    skull_bot.sendMessage(game.game_id, msg)


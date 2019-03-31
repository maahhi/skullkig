import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
skull_bot = telepot.Bot("754043278:AAEvIPHV-1t_yxooOuUUs4DMbqj2EbhqT_Q")


def showInPV(player, choice):
    text = ""
    for card in choice:
        text += (str(list(card.keys())[0]) + " " + str(list(card.values())[0]) + "\n")
    skull_bot.sendMessage(player.id, text)


def askInPV(player, dast):
    button_list = []
    for item in dast:
        i = str(item)
        print(i)
        button_list.append(InlineKeyboardButton(text=i, callback_data='press'))
        print(button_list)
    qkeyboard = InlineKeyboardMarkup(inline_keyboard=[button_list])
    skull_bot.sendMessage(player.id, "This is your dast!", reply_markup=qkeyboard)


def showInGroup(game, input, description):
    skull_bot.sendMessage(game.game_id, "This is an incomplete function!")

import telepot

skull_bot = telepot.Bot("754043278:AAEvIPHV-1t_yxooOuUUs4DMbqj2EbhqT_Q")

def ask_in_pv(player, choice):
    skull_bot.sendMessage(player.id, "Choose! between them!")


def show_in_pv(player, dast):
    skull_bot.sendMessage(player.id, "This is your dast!")


def show_in_group(input, description):
    skull_bot.sendMessage("This is an incomplete function!")
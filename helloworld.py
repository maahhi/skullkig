import telepot
token = '123456'
TelegramBot = telepot.Bot("750131965:AAFWhgqc_h8ejEpIfPtL_8EAC8IGN3aVKwE")
import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '750131965:AAFWhgqc_h8ejEpIfPtL_8EAC8IGN3aVKwE'
    bot_chatID = '67384197'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import random
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '<Hide Token>'
max_team = 9

bot = telebot.TeleBot(API_TOKEN)
is_called = False


# Handle '/start' and '/help'
@bot.message_handler(commands=['shuffle'])
def send_welcome(message):
    global is_called
    if is_called:
        return
    is_called = True
    bot.send_message(message.chat.id, """\
開拓者小隊你們好，系統即將產出 Hackathon 的順序...\
""")
    order = list(range(1, max_team + 1))
    random.shuffle(order)
    time.sleep(1.5)
    mes = bot.send_message(message.chat.id, ("你們的順序是：...")).id
    for i in range(len(order)):
        time.sleep(0.5)
        bot.edit_message_text("你們的順序是：{}...".format(order[:i]), message.chat.id, mes)
        #bot.send_message(message.chat.id, o)
        
    bot.edit_message_text(("你們的順序是：{}".format(order)), message.chat.id, mes)
    time.sleep(0.5)
    bot.pin_chat_message(message.chat.id, mes)
    time.sleep(1.5)
    gif_url = "https://media.giphy.com/media/3oEjHKPPlmQlGXfeLK/giphy.gif"
    gif_caption = "過...載...\n{}".format(gif_url)
    bot.send_document(message.chat.id, gif_url, caption=gif_caption)
    time.sleep(0.5)
    bot.leave_chat(message.chat.id)

bot.infinity_polling()
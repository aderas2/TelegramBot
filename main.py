import os
import telebot

my_secret = os.environ['API_KEY']

bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=["greet"])
def greet(message):
  bot.reply_to (message, "Hey! You are welcome!")

@bot.message_handler(commands=["name"])
def name(message):
  bot.send_message (message.chat.id, "Aderas")

bot.polling()





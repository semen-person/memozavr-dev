import telebot

from telebot import types

TOKEN = '1017092229:AAGfakUe7TMHtP8MwTDhS6hYXD8wHEmK9X0' # bot token OKDA

bot = telebot.TeleBot(TOKEN)

#memes

def nice(message):

	noice = open('img/noice.jpg', 'rb')

	bot.send_photo(message.chat.id, noice)

	bot.send_message(message.chat.id, "Держи, ёмаё.")

	print("[LOG] Noice meme sent to", message.chat.id, "(Chat ID)")
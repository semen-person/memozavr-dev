import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])

def starting(message):

	print("[LOG] Message from bot to ", message.chat.id, "(Chat ID) sent (New user)")

	bot.send_message(message.chat.id, "Хей! Я - Мемозавр. Напиши мне слово и я отправлю тебе картинку!")


@bot.message_handler(content_types=['text'])

def main(message):

	

	if message.text == 'nice':

		config.nice(message)

	elif message.text == 'noice':

		config.nice(message)

	else:

		bot.send_message(message.chat.id, "я токих мемоф низнаю. Я пока ни оч много мемовф знаюб.")

		


###################################################################

bot.polling(none_stop=True)
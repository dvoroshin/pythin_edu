import telebot
import requests

bot = telebot.TeleBot(
    "6167539394:AAGnl656I4HJYLRCoM2YQcVvNa_Mk5-sKcc", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как дела?")

@bot.message_handler(commands=['reg'])
def registration_procedure(message):
    data = open('registration.txt', 'r', encoding='utf-8')
    bot.
    data.close()
    bot.reply_to(message, "Привет, как дела?")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'погода':
        data = requests.get('https://wttr.in/?format=3')
        bot.reply_to(message, data.text)
    elif message.text == 'кот':
        cat = open('C:/Users/voroshin/Pictures/kot.jpg', 'rb')
        # print(message)
        bot.send_photo(message.from_user.id, cat)
    else:
        print(message.text)

bot.infinity_polling()
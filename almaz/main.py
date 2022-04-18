import telebot
TOKEN = '5319894674:AAFGaJY4rvIy37QpcVZAcrCdp8zImqaIkzo'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.id == 944933015:
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, рад приветствовать тебя в нашей команде!\n ".format(message.from_user, bot.get_me()), parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Извини, {0.first_name}!\nУ тебя нет доступа(\n ".format(message.from_user), parse_mode='html')
@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text == "Как дела?":
        bot.send_message(message.chat.id, "Все ок")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)

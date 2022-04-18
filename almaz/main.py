import telebot
import id_filter
import my_token

bot = telebot.TeleBot(my_token.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if id_filter.id_filter(message.from_user.id):
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, рад приветствовать тебя в нашей команде!\n ".format(message.from_user, bot.get_me()), parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Извини, {0.first_name}!\nУ тебя нет доступа(\n ".format(message.from_user), parse_mode='html')

@bot.message_handler(content_types=['text'])
def echo(message):
    if id_filter.id_filter(message.from_user.id) == False:
        bot.send_message(message.chat.id, "Извини, {0.first_name}!\nУ тебя нет доступа(\n ".format(message.from_user), parse_mode='html')
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, "Все ок")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)



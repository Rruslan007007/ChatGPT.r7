import telebot

# Ваш токен, который вы получили от BotFather
TOKEN = '7404318756:AAEOyOeSEw2zSsOEZp5O2MjSThD6YNxaA88'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling(none_stop=True)

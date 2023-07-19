import telebot
import webbrowser
from telegram.ext import Updater, CommandHandler


TOKEN = '6143029161:AAH9jjZPe5daGn_kn6hd8AqTirIchaUqVr8'
updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher
bot = telebot.TeleBot('6143029161:AAH9jjZPe5daGn_kn6hd8AqTirIchaUqVr8')
updater.bot.send_document()


def call_back(update, context):
    bot.send_document(chat_id=chat_id, document=open('tests/test.png', 'rb'))


@bot.message_handlers(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://hh.ru/resume/224aedf8ff0bdd01aa0039ed1f6d356c49724f?from=share_ios')


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f' Hello {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def mmes(message):
    bot.send_message(message.chat.id, f'{message}')


@bot.message_handlers()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f' Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id: {message.from_user.id}')


bot.polling(none_stop=True)
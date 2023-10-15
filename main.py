import telebot 
from config import token

from logic import Pocemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pocemon.pocemons.keys():
        pocemon = Pocemon(message.from_user.username)
        bot.send_message(message.chat.id, pocemon.info())
        bot.send_photo(message.chat.id, pocemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)


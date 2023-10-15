import telebot 
from config import token

from logic import Pocemon

bot = telebot.TeleBot(token) 

pocemons = {}

@bot.message_handler(commands=['go'])
def start(message):
    global pocemons 

    if message.from_user.username not in pocemons.keys():
        pocemon = Pocemon(message.from_user.username)
        pocemons[message.from_user.username] = pocemon
        bot.send_message(message.chat.id, pocemon.info())
        bot.send_photo(message.chat.id, pocemon.show_img())
        
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)


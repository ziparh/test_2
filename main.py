import telebot 
from random import randint
from config import token
from functools import wraps

from logic import Pokemon, Wizard, Fighter

def has_pokemon(func):
    @wraps(func)
    def wraper(message):
        if message.from_user.username in Pokemon.pokemons.keys():
            return func(message)
        else:
            bot.reply_to(message, "Для начала тебе нужно создать себе покемона, нажимай - /go")
    return wraper

def no_pokemon(func):
    @wraps(func)
    def wraper(message):
        if message.from_user.username not in Pokemon.pokemons.keys():
            return func(message)
        else:
            bot.reply_to(message, "Ты уже создал себе покемона")
    return wraper

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['info'])
@has_pokemon
def info_pok(message):
    pok = Pokemon.pokemons[message.from_user.username]
    res = pok.info()
    bot.send_message(message.chat.id, res)

# @bot.message_handler(commands=['info'])
# def info_pok(message):
#     if message.from_user.username in Pokemon.pokemons.keys():
#         pok = Pokemon.pokemons[message.from_user.username]
#         res = pok.info()
#         bot.send_message(message.chat.id, res)
#     else:
#         bot.reply_to(message, "Для начала тебе нужно создать себе покемона, нажимай - /go")


@bot.message_handler(commands=['feed'])
@has_pokemon
def feed_pok(message):
    pok = Pokemon.pokemons[message.from_user.username]
    res = pok.feed()
    bot.send_message(message.chat.id, res)

@bot.message_handler(commands=['go'])
@no_pokemon
def go(message):
    if randint(1, 2) == 1:
        pokemon = Fighter(message.from_user.username)
    else:
        pokemon = Wizard(message.from_user.username)
    bot.send_message(message.chat.id, pokemon.info())
    bot.send_photo(message.chat.id, pokemon.show_img())


@bot.message_handler(commands=['fight'])
def fight_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.fight(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
        bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для игры в покемонов, скорее попробуй создать себе покемона, нажимай - /go")


bot.infinity_polling(none_stop=True)


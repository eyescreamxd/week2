from ephem import *
import logging
import re
from setting import API_KEY
from cities import cities_list
from user_data import user_data
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def cities(bot, update):
    # print(update)
    # print(update.message.from_user.username)
    if update.message.from_user.username not in user_data:
        user_data[update.message.from_user.username] = []
        user_data[update.message.from_user.username].append(update.message.text[8:])
        print(user_data)
    else:
        user_data[update.message.from_user.username].append(update.message.text[8:])
        print(user_data)

def word_counter(bot, update):
    update.message.reply_text(len(re.findall(r'[a-zA-Z0-9а-яА-Я]+', update.message.text)) - 1)


def tg_next_full_moon(bot, update):
    if len(update.message.text.split()) == 1:
        update.message.reply_text(next_full_moon(update.message.date))
    else:
        update.message.reply_text(next_full_moon(update.message.text.split()[-1]))


def check_planet(bot, update):
    planet = str(update.message.text.split(' ')[1]).lower()
    if planet == 'mercury':
        update.message.reply_text(constellation(Mercury(now()))[-1])
    elif planet == 'venus':
        update.message.reply_text(constellation(Venus(now()))[-1])
    elif planet == 'mars':
        update.message.reply_text(constellation(Mars(now()))[-1])
    elif planet == 'jupiter':
        update.message.reply_text(constellation(Jupiter(now()))[-1])
    elif planet == 'saturn':
        update.message.reply_text(constellation(Saturn(now()))[-1])
    elif planet == 'uranus':
        update.message.reply_text(constellation(Uranus(now()))[-1])
    elif planet == 'neptune':
        update.message.reply_text(constellation(Neptune(now()))[-1])


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", check_planet))
    dp.add_handler(CommandHandler("wordcount", word_counter))
    dp.add_handler(CommandHandler("next_full_moon", tg_next_full_moon))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

from ephem import *
import logging
import re
import random
from setting import API_KEY
from week2.cities import cities_list

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='bot.log'
                    )
user_data = {}  # {'username': ['city1', 'city2']} ключ — %username%; значение — список использованных названий городов в рамках раунда с конкретным пользователем


def cities(bot, update):

    user = update.message.from_user.username  # выхватываем %username% из сообщения
    city = update.message.text[8:].lower()  # выхватываем всё, кроме комманды
    last_letter = city[-1]  # объявляем последнюю букву из названия города, на которую мы будем отвечать

    if city not in cities_list:  # проверка, если названия города пользователя нет в списке городов
        update.message.reply_text('Не знаю такого города. Давай другой.')
    else:
        if last_letter in 'ыъйь':  # если название города заканчивается на одну из указанных букв, то берём предпоследнюю
            last_letter = city[-2]

        if user not in user_data or len(user_data[user]) == 0:  # если пользователя нет в словаре
            user_data[user] = []   # инициализация пустого списка для ключа %username%
            user_data[user].append(city)  # добавляем в список название города, которое прислал юзер
            bot_city = random.choice([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]])  # составляем список названий городов, которые начинаются на нужную букву и не были использованы. Выбираем рандомное название города
            update.message.reply_text(bot_city)  # отвечаем рандомным названием
            user_data[user].append(bot_city)  # добавляем рандомное название в список использованных для этого юзера
        else:
            if len(cities_list) == len(user_data[user]):  # если длина списка использованных названий городов равна длине известных городов, то прекращаем игру
                update.message.reply_text('Известные мне города закончились. Обнуляем список городов.')
                user_data[user] = []  # обнуляем список использованных названий городов
            elif len([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]]) == 1:  # если закончился список известных городов на определённую букву, то также прекращаем игру
                random.choice([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]])  # отсылаем последнее название города
                update.message.reply_text('Использовано последнее слово на эту букву, которое я знаю. Начинаем сначала')
                user_data[user] = []  # обнуляем список
            else:
                start_letter = user_data[user][-1][-1]  # объявляем букву, на которую должен ответить пользователь
                if start_letter in 'ыъйь':  # если название города заканчивается на одну из указанных букв, то берём предпоследнюю
                    start_letter = user_data[user][-1][-2]

                if start_letter != city[0]:  # если название города пользователя начинается не с той буквы, ругаем его
                    update.message.reply_text('Схитрить решил? Отвечай честно!')
                else:
                    if city in user_data[user]:  # если название города уже было использовано, ругаем пользователя
                        update.message.reply_text('Схитрить решил? Отвечай честно!')
                    else:
                        user_data[user].append(city)  # добавляем название города в список использованных в этой сессии юзера
                        bot_city = random.choice([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]])  # выбираем рандомный город, который начинается с последней буквы
                        update.message.reply_text(bot_city)  # отвечаем городом
                        user_data[user].append(bot_city)  # добавляем город в список
                        print(user_data[user])


def calc(update, context):
    user = update.message.from_user.username
    try:
        user_text = str(update.message.text).split()[-1]
        if ',' in user_text:
            user_text = user_text.replace(',', '.')

        if re.findall('(\d+).+?(\d+)', user_text):
            update.message.reply_text(f"Ответ: {eval(user_text)}")
        else:
            update.message.reply_text(f"Что-то ты мне прислал ерунду какую-то.\n"
                                      f"Пиши /calc и пример, который должен решить, а не вот это вот все.\n")
    except TypeError:
        update.message.reply_text(f"Не понимаю как это решить. Попробуй написать пример по-другому.")
    except ZeroDivisionError:
        update.message.reply_text(f"Себя на 0 подели. Школьную математику забыл?")
    except SyntaxError:
        update.message.reply_text(f"У тебя в примере, это... Ошибка есть. Давай по новой, {user}.")


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
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

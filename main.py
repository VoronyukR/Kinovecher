import telebot
from telebot import types
from telebot import TeleBot
from bs4 import BeautifulSoup as bs
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import numpy as np
import pandas as pd
import random
import requests
import csv

token = '5701044691:AAHd73k1Gvgl1U3QCke6F6htXBgLYhdP1Gc'
bot = telebot.TeleBot(token)

amogus = list()
client_status = {}
l = list()
char = []
char_2 = []


@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup1.add(types.KeyboardButton("Я не знаю, что посмотреть"))
    markup1.add(types.KeyboardButton("Я знаю, что посмотреть, но не могу определиться"))
    markup1.add(types.KeyboardButton("Я хочу посмотреть одно, а моя вторая половинка - другое"))
    bot.send_message(message.chat.id, f'<b>Приветствую, {message.from_user.first_name}.\nЧто вы хотите сделать?</b>', parse_mode='html', reply_markup=markup1)
    amogus.clear()
    char.clear()

@bot.message_handler(commands=['menu'])
def menu(message):
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_menu.add(types.KeyboardButton("Я не знаю, что посмотреть"))
    markup_menu.add(types.KeyboardButton("Я знаю, что посмотреть, но не могу определиться"))
    markup_menu.add(types.KeyboardButton("Я хочу посмотреть одно, а моя вторая половинка - другое"))
    bot.send_message(message.chat.id, f'Что вы хотите сделать?', reply_markup=markup_menu)
    amogus.clear()
    char.clear()
    char_2.clear()


# @bot.message_handler(commands=['game'])
# def game(message):
#     markup_game = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup_begin = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     lvl_1 = types.KeyboardButton('Легкий')
#     lvl_2 = types.KeyboardButton('Средний')
#     lvl_3 = types.KeyboardButton('Сложный')
#     begin = types.KeyboardButton('Начать')
#     markup_game.add(lvl_1, lvl_2, lvl_3)
#     markup_begin.add(begin)
#     bot.send_message(message.chat.id, 'Выберите режим игры', reply_markup=markup_game)
#     if message.text == 'Легкий':
#         bot.send_message(message.chat.id, 'Вы должны будете угадать фильм по описанию', reply_markup=markup_begin)
#         if message.text == 'Начать':
#             with open('data.csv', 'r') as file:
#                 reader = csv.reader(file)
#                 for row in reader:
#
#
#     elif message.text == 'Средний':
#         pass
#     elif message.text == 'Сложный':
#         pass


@bot.message_handler(func=lambda message: message.text == "Вернуться назад")
def back_main(message):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup2.add(types.KeyboardButton("Я не знаю, что посмотреть"))
    markup2.add(types.KeyboardButton("Я знаю, что посмотреть, но не могу определиться"))
    markup2.add(types.KeyboardButton("Я хочу посмотреть одно, а моя вторая половинка - другое"))
    bot.send_message(message.chat.id, f'Что вы хотите сделать?', reply_markup=markup2)
    amogus.clear()
    char.clear()


def back_main2(message):
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    randomize_but = types.KeyboardButton('Я хочу, чтобы ты выбрал за меня')
    read_but = types.KeyboardButton('Я хочу прочитать описание фильма')
    back = types.KeyboardButton("Вернуться назад")
    markup3.row(randomize_but, read_but)
    markup3.add(back)
    bot.send_message(message.chat.id, f'Что вам подходит больше?', reply_markup=markup3)


@bot.message_handler(content_types=['Я хочу, чтобы ты выбрал за меня'])
def _command_(message):
    bot.register_next_step_handler(message, add_user)
def add_user(message):
    amogus = message.text.split(',')
    markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton("Вернуться назад")
    repeat = types.KeyboardButton('Еще раз')
    markup5.add(back, repeat)
    bot.send_message(message.chat.id, amogus[random.randrange(len(amogus))], reply_markup=markup5)
    pass


@bot.message_handler(content_types=['Я хочу посмотреть одно, а моя вторая половинка - другое'])
def _command_1(message):
    bot.register_next_step_handler(message, add_user_1)
def add_user_1(message):
    l = []
    fillist = []
    s = str()
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back0 = types.KeyboardButton('Вернуться назад')
    repeat0 = types.KeyboardButton('Попробовать снова')
    markup0.add(back0, repeat0)
    char = message.text.split(',')
    bot.send_message(message.chat.id, text='Одну секунду...')
    if len(char) == 1:
        bot.send_message(message.chat.id, f'Вы написали только один фильм', reply_markup=markup0)
    elif len(char) > 2:
        bot.send_message(message.chat.id, f'Вы написали больше двух фильмов', reply_markup=markup0)
    else:
        msg1 = char[0].strip()
        msg2 = char[1].strip()
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if msg1 == row[0] or msg2 == row[0]:
                    l.append(row[3].split(',')[0].strip())
        for i in range(len(l)):
            if l[i] in l[:i]:
                l.pop(i)
        for i in range(len(l)):
            if len(l) == i + 1:
                s = s + l[i]
            else:
                s = s + l[i] + ', '
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if s == row[3] and msg1 not in row and msg2 not in row:
                    fillist.append(row)
            if len(fillist) > 0:
                film_1 = fillist[random.randrange(len(fillist))]
                film_name, film_year, film_rate, film_Genre, film_image, film_href = film_1
                bot.send_photo(message.chat.id, film_image, caption=f'Ваш идеальный фильм:\n\n<b>{film_name}</b> \n'
                                                  f'Жанр: {film_Genre}\n'
                                                  f'Год выпуска: {film_year}\n'
                                                  f'Оценка: {film_rate}', parse_mode='html', reply_markup=markup0)

            else:
                bot.send_message(message.chat.id, text=f'У вас очень специфические вкусы, попробуйте что-нибудь другое', reply_markup=markup0)
pass

@bot.message_handler(content_types=['Я хочу прочитать описание фильмa'])
def _command_2(message):
    bot.register_next_step_handler(message, add_user_2)

def add_user_2(message):
    film_i = 0
    error = 0
    char_2 = message.text.split(',')[0]
    markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton("Вернуться назад")
    repeat = types.KeyboardButton('Повторить поиск')
    markup8.add(back, repeat)
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            error +=1
            if char_2 == row[0]:
                film_url = row[5]
                req = requests.get(film_url)
                soup = bs(req.text, 'html.parser')
                ann = soup.find_all('div', class_='visualEditorInsertion filmDesc_editor more_content')[film_i].text
                bot.send_photo(message.chat.id, row[4])
                bot.send_message(message.chat.id, f"<b>О фильме \"{char_2}\"</b>\n{ann}", parse_mode='html', reply_markup=markup8)
                error -=1
            if error == 2000:
                bot.send_message(message.chat.id, f'Извините, фильм \"{char_2}\" мне не знаком', reply_markup=markup8)
        film_i+=1


@bot.message_handler(content_types=['text'])
def message_reply1(message):
    if message.text == 'Я не знаю, что посмотреть':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        battlebut = types.KeyboardButton("Боевик")
        dramabut = types.KeyboardButton("Драма")
        combut = types.KeyboardButton("Комедия")
        trilbut = types.KeyboardButton("Триллер")
        detbut = types.KeyboardButton("Детектив")
        fantbut = types.KeyboardButton("Фантастика")
        fentbut = types.KeyboardButton("Фэнтези")
        uzhbut = types.KeyboardButton("Ужасы")
        sembut = types.KeyboardButton("Семейный")
        back = types.KeyboardButton("Вернуться назад")
        markup.row(battlebut, dramabut, combut)
        markup.row(trilbut, detbut, fantbut,)
        markup.row(fentbut, uzhbut, sembut)
        markup.add(back)
        bot.send_message(message.chat.id, f'Выберите жанр:', reply_markup=markup)
    if message.text == 'Боевик' or message.text =='Драма' or message.text =='Комедия' or message.text =='Триллер' or message.text =='Детектив' or message.text =='Фантастика' or message.text =='Фэнтези' or message.text =='Ужасы' or message.text =='Семейный':
        with open('data.csv', newline='') as File:
            reader = csv.reader(File)
            genre_list = []
            for row in reader:
                if message.text.lower() in row[3]:
                    genre_list.append(row)
            film = genre_list[random.randrange(len(genre_list))]
            film_name, film_year, film_rate, film_Genre, film_image, film_href = film
            bot.send_photo(message.chat.id, film_image, caption=f'Ваш фильм жанра {message.text.lower()} на вечер:\n\n<b>{film_name}</b> \n'
                                              f'Жанр: {film_Genre}\n'
                                              f'Год выпуска: {film_year}\n'
                                              f'Оценка: {film_rate}', parse_mode='html')
    if message.text == 'Я знаю, что посмотреть, но не могу определиться':
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        randomize_but = types.KeyboardButton('Я хочу, чтобы ты выбрал за меня')
        read_but = types.KeyboardButton('Я хочу прочитать описание фильмa')
        back = types.KeyboardButton("Вернуться назад")
        markup3.row(randomize_but, read_but)
        markup3.add(back)
        bot.send_message(message.chat.id, f'Что вам подходит больше?', reply_markup=markup3)
    if message.text == 'Я хочу, чтобы ты выбрал за меня':
        markup4 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите названия фильмов через запятую: ", reply_markup=markup4)
        _command_(message)
    if message.text == 'Еще раз':
        markup4 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите названия фильмов через запятую: ", reply_markup=markup4)
        _command_(message)
    if message.text == 'Я хочу прочитать описание фильмa':
        markup5 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Введите название фильма:', reply_markup=markup5)
        _command_2(message)
    if message.text == 'Повторить поиск':
        markup4 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите название фильма: ", reply_markup=markup4)
        _command_2(message)
    if message.text == 'Я хочу посмотреть одно, а моя вторая половинка - другое':
        markup6 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите название фильмов, которые хотите посмотреть, через запятую:\nМаксимум: 2 фильма", reply_markup=markup6)
        _command_1(message)
    if message.text == 'Попробовать снова':
        markup6 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите название фильмов, которые хотите посмотреть, через запятую:\nМаксимум: 2 фильма", reply_markup=markup6)
        _command_1(message)

bot.infinity_polling()


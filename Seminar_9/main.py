
from telebot import TeleBot, types
import os
from keyboard import *
from keyboard_Phone import *
from log import log
from calculator import check_j, ration, result
from functions import input_console, read_file, write_file, input_file, read_input_file, search_user_phone, delet_user, write_html, read_input_file_html, mutationes_user_phone, input_mutationes

 
TOKEN = ''
 
bot = TeleBot(TOKEN)

value = ''
old_value = ''
search_index = -1


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    log(f'user_id: {msg.from_user.id}, user_name: {msg.from_user.first_name}, text: {msg.text}, message_id: {msg.message_id}')
    bot.send_message(chat_id=msg.from_user.id, text=f'/start и /help - Начало работы с ботом, вывод списка комманд')
    bot.send_message(chat_id=msg.from_user.id, text=f'/calc - Начать работу с калькулятором')
    bot.send_message(chat_id=msg.from_user.id, text=f'/Phone - Начать работу с телефонным справочником')


@bot.message_handler(commands=['calc'])
def calc(msg):
    log(f'user_id: {msg.from_user.id}, user_name: {msg.from_user.first_name}, text: {msg.text}, message_id: {msg.message_id}')
    global value
    if value == '':
        bot.send_message(chat_id=msg.from_user.id, text='0', reply_markup=keyboard)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'{value}', reply_markup=keyboard)


@bot.message_handler(commands=['Phone'])
def phone(msg):
    log(f'user_id: {msg.from_user.id}, user_name: {msg.from_user.first_name}, text: {msg.text}, message_id: {msg.message_id}')
    bot.send_message(chat_id=msg.from_user.id, text='Главное меню', reply_markup=keyboard_phone)



@bot.callback_query_handler(func=lambda call:True)
def callback_func(query):
    global value, old_value
    data = query.data
    mes = query.message
    
    log(f'пользователь нажал кнопку: {data}')

    if data == 'Ввод данных':
        bot.send_message(chat_id=query.from_user.id, text='Меню ввода информации', reply_markup=keyboard_input)
    elif data == 'Редактировать':
        bot.send_message(chat_id=query.from_user.id, text='Меню редактирования', reply_markup=keyboard_edit)
    elif data == 'Выход в главное меню':
        bot.send_message(chat_id=query.from_user.id, text='Главное меню', reply_markup=keyboard_phone)
    elif data == 'Экспорт данных из файла':
        bot.send_message(chat_id=query.from_user.id, text='Меню экспорта данных', reply_markup=keyboard_export)
    elif data == 'Вывод списка на экран':
        bot.send_message(chat_id=query.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)
    elif data == 'Ввод данных с клавиатуры':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Ввод данных с клавиатуры.\n Введите данные в формате: \nИмя;Фамилия;Телефон;Комментарий')
        bot.register_next_step_handler(mes, user_add_manual)
    elif data == 'Импорт данных из файла':
        bot.send_message(chat_id=query.from_user.id, text='Меню импорта данных из файла', reply_markup=keyboard_input_file)
    elif data == 'Импорт из файла "csv"':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Импорт данных из файла.\n Прикрепите файл в чате.')
        bot.register_next_step_handler(mes, user_add_file)
    elif data == 'Импорт из файла "html"':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Импорт данных из файла.\n Прикрепите файл в чате.')
        bot.register_next_step_handler(mes, user_add_file_html)
    elif data == 'Экспортировать файл "csv"':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Экспортировать файл в формате "csv".')
        bot.send_document(chat_id=query.from_user.id, document=open('base.csv', 'rb'))
        log(f'пользователю отправлен файл: base.csv')
        bot.send_message(chat_id=query.from_user.id, text='Меню экспорта данных', reply_markup=keyboard_export)
    elif data == 'Экспортировать файл "xml"':
        bot.send_message(chat_id=query.from_user.id, text=f'Экспорт файла в формате "xml" находится в разработке.')# РАЗРАБОТАТЬ и поменять заглушку
        bot.send_message(chat_id=query.from_user.id, text='Меню экспорта данных', reply_markup=keyboard_export)
    elif data == 'Экспортировать файл "html"':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Экспортировать файл в формате "html".')
        array = read_file()
        write_html(array)
        bot.send_document(chat_id=query.from_user.id, document=open('base.html', 'rb'))
        os.remove('base.html')
        bot.send_message(chat_id=query.from_user.id, text='Меню экспорта данных', reply_markup=keyboard_export)
    elif data == 'Удалить пользователя':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Удалить пользователя.')
        bot.send_message(chat_id=query.from_user.id, text=f'Введите номер телефона в чате.')
        bot.register_next_step_handler(mes, delete_user)
    elif data == 'Редактировать данные':
        bot.send_message(chat_id=query.from_user.id, text=f'Введите номер телефона в чате.')
        bot.register_next_step_handler(mes, search_mutationes_user)
        #bot.send_message(chat_id=query.from_user.id, text='Меню редактирования', reply_markup=keyboard_edit)
    elif data == 'Печать всего списка':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Печать всего списка.')
        array = read_file()
        for data in array:
            bot.send_message(chat_id=query.from_user.id, text='\n'.join(data))
        log(f'пользователю отправлен в чат список пользователей')
        bot.send_message(chat_id=query.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)
    elif data == 'Поиск по номеру телефона':
        bot.send_message(chat_id=query.from_user.id, text=f'Вы выбрали: Поиск по номеру телефона.')
        bot.send_message(chat_id=query.from_user.id, text=f'Введите номер телефона в чате.')
        bot.register_next_step_handler(mes, phone_search)
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        log(f'Значение value = {value}')
        
        try:
            value = result(ration(value), check_j(value))
            log(f'результат вычислений (рациональное)= {value}')
        except:
            value = 'Ошибка!'
        
    else:
        value += data
    
    if data not in lst_text:
        if (value != old_value and value != '') or ('0' != old_value and value == ''):
            if value == '':
                bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text='0', reply_markup=keyboard)
                old_value = '0'
            else:
                bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=value, reply_markup=keyboard)
                old_value = value
    
    if value == 'Ошибка!':
        value = ''


def delete_user(msg: types.Message):# Поиск пользователя по номеру телефона и удаление его из базы
    array = read_file()
    delet_array = delet_user(array, msg.text)
    if delet_array:
        log(f'Найден пользователь с искомым номером телефона {msg.text} и удален')
        write_file(delet_array)
        bot.send_message(chat_id=msg.from_user.id, text='Пользователь с таким номером телефона удален.')
    else:
        log(f'Пользователь с номером телефона {msg.text} не найден')
        bot.send_message(chat_id=msg.from_user.id, text='Пользователь с таким номером телефона не найден.')
    


def search_mutationes_user(msg: types.Message):# Поиск пользователя по номеру телефона и определения номера индекса в списке
    global search_index
    array = read_file()
    search_index = mutationes_user_phone(array, msg.text)
    if search_index != -1:
        log(f'Найден пользователь с искомым номером телефона: {msg.text} => {search_index}')
        bot.send_message(chat_id=msg.from_user.id, text=f'Пользователь с номером телефона ({msg.text}) найден.')
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите новые данные пользователя в формате: \nИмя;Фамилия;Телефон;Комментарий')
        bot.register_next_step_handler(msg, mutationes_user)
    else:
        log(f'Пользователь с номером телефона {msg.text} не найден')
        bot.send_message(chat_id=msg.from_user.id, text='Пользователь с таким номером телефона не найден.')
        bot.send_message(chat_id=msg.from_user.id, text='Меню редактирования', reply_markup=keyboard_edit)


def mutationes_user(msg: types.Message):# Внесение изменений в данные пользователя по найденному в методе search_mutationes_user индексу
    global search_index

    array = read_file()
    arr = input_mutationes(array, msg.text)
    array[search_index] = arr
    write_file(array)
    bot.send_message(chat_id=msg.from_user.id, text=f'Данные пользователя успешно изменены!.')
    bot.send_message(chat_id=msg.from_user.id, text='Меню редактирования', reply_markup=keyboard_edit)

    
    #bot.send_message(chat_id=msg.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)


def phone_search(msg: types.Message):# Поиск и вывод на экран пользователя с искомым номером телефона
    array = read_file()
    search = mutationes_user_phone(array, msg.text) 
    if search:
        log(f'Найден пользователь с искомым номером телефона: {msg.text} => {search}')
        bot.send_message(chat_id=msg.from_user.id, text='\n'.join(search))
    else:
        log(f'Пользователь с номером телефона {msg.text} не найден')
        bot.send_message(chat_id=msg.from_user.id, text='Пользователь с таким номером телефона не найден.')
    bot.send_message(chat_id=msg.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)


def user_add_file_html(msg: types.Message):# Импортирует данные из файла html
    filename = msg.document.file_name
    log(f'пользователь прислал файл: {filename}')
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text=f'Файл {filename} успешно получен.')
    array_file = read_input_file_html(filename)
    os.remove(filename)
    log(f'Данные из файла: {filename} успешно считаны. Файл {filename} удален')
    array_base = read_file()
    array = input_file(array_base, array_file)
    write_file(array)
    bot.send_message(chat_id=msg.from_user.id, text=f'Импорт файла {filename} выполнен успешно.')
    bot.send_message(chat_id=msg.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)
    log(f'Файл: {filename} импортирован')


def user_add_file(msg: types.Message):# Импортирует данные из файла csv
    filename = msg.document.file_name
    log(f'пользователь прислал файл: {filename}')
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text=f'Файл {filename} успешно получен.')
    array_file = read_input_file(filename)
    os.remove(filename)
    log(f'Данные из файла: {filename} успешно считаны. Файл {filename} удален')
    array_base = read_file()
    array = input_file(array_base, array_file)
    write_file(array)
    bot.send_message(chat_id=msg.from_user.id, text=f'Импорт файла {filename} выполнен успешно.')
    bot.send_message(chat_id=msg.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)
    log(f'Файл: {filename} импортирован')


def user_add_manual(msg: types.Message):# Считывание из базы, добавление новых пользывателей в ручную и запись в базу
    log(f'пользователь ввел данные нового пользователя: {msg}')
    array = read_file()
    arr = input_console(array, msg.text)
    if arr:
        write_file(arr)
        bot.send_message(chat_id=msg.from_user.id, text=f'Данные успешно сохранены.')
        bot.send_message(chat_id=msg.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)
        log(f'Новый пользователь: {msg} добавлен в базу данных')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Пользователь с такими данными уже есть!')
        bot.send_message(chat_id=msg.from_user.id, text='Меню вывода информации', reply_markup=keyboard_print)
        log(f'пользователь: {msg} уже был в базе данных')
  
 
bot.polling() # Отправляет запрос на сервер телеграмм(небыло ли для меня сообщений?)

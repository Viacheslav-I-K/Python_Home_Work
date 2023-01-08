from telebot import TeleBot, types


keyboard_phone = types.InlineKeyboardMarkup()
keyboard_phone.row(   types.InlineKeyboardButton('Ввод данных', callback_data='Ввод данных'),
                    types.InlineKeyboardButton('Редактировать', callback_data='Редактировать'))
keyboard_phone.row(   types.InlineKeyboardButton('Экспорт данных из файла', callback_data='Экспорт данных из файла'),
                    types.InlineKeyboardButton('Вывод списка на экран', callback_data='Вывод списка на экран'))


keyboard_input = types.InlineKeyboardMarkup()
keyboard_input.row(   types.InlineKeyboardButton('Ввод данных с клавиатуры', callback_data='Ввод данных с клавиатуры'),
                    types.InlineKeyboardButton('Импорт данных из файла', callback_data='Импорт данных из файла'))
keyboard_input.row(   types.InlineKeyboardButton('Выход в главное меню', callback_data='Выход в главное меню'))


keyboard_edit = types.InlineKeyboardMarkup()
keyboard_edit.row(   types.InlineKeyboardButton('Удалить пользователя', callback_data='Удалить пользователя'),
                    types.InlineKeyboardButton('Редактировать данные', callback_data='Редактировать данные'))
keyboard_edit.row(   types.InlineKeyboardButton('Выход в главное меню', callback_data='Выход в главное меню'))


keyboard_print = types.InlineKeyboardMarkup()
keyboard_print.row(   types.InlineKeyboardButton('Печать всего списка', callback_data='Печать всего списка'),
                    types.InlineKeyboardButton('Поиск по номеру телефона', callback_data='Поиск по номеру телефона'))
keyboard_print.row(   types.InlineKeyboardButton('Выход в главное меню', callback_data='Выход в главное меню'))


keyboard_export = types.InlineKeyboardMarkup()
keyboard_export.row(   types.InlineKeyboardButton('Экспортировать файл "csv"', callback_data='Экспортировать файл "csv"'),
                    types.InlineKeyboardButton('Экспортировать файл "xml"', callback_data='Экспортировать файл "xml"'))
keyboard_export.row(   types.InlineKeyboardButton('Экспортировать файл "html"', callback_data='Экспортировать файл "html"'),
                    types.InlineKeyboardButton('Выход в главное меню', callback_data='Выход в главное меню'))


lst_text = ['Ввод данных', 'Редактировать', 'Экспорт данных из файла', 'Вывод списка на экран', 'Ввод данных с клавиатуры', 'Импорт данных из файла', 'Выход в главное меню',
 'Удалить пользователя', 'Редактировать данные', 'Печать всего списка', 'Поиск по номеру телефона', 'Экспортировать файл "csv"',
 'Экспортировать файл "xml"', 'Меню вывода информации', 'Экспортировать файл "html"']
import datetime


def log(string):
   time = datetime.datetime.now()
   with open('logfile.txt', 'a', encoding='utf-8') as log:
      log.write(f'Время события: {time}; Содержание события: {string};\n')

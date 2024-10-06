import os
import time

os.chdir('.')
print(os.getcwd())
directory = '.'

for dirpath, dirnames, filenames in os.walk(directory):

    for files in filenames:

        path = os.path.join(dirpath, files)

        file_time = os.path.getmtime(path)

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))

        file_size = os.path.getsize(path)

        dir_name = os.path.dirname(path)

        print(f'Обнаружен файл: {files}, Путь: {path}, Размер: {file_size} байт, Время изменения: {formatted_time}'
              f'Родительская директория: {dir_name}')
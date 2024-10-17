from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for cnt in range(word_count):
            file.write(f'Какое-то слово № {cnt}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        res = func(*args, **kwargs)
        print(f'Время выполнения {func.__name__}: {datetime.now() - start_time}')
        return res
    return wrapper

@execution_time
def func_write():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

@execution_time
def thread_write():
    thread_one = Thread(target=write_words, args=(10, 'example5.txt'))
    thread_two = Thread(target=write_words, args=(30, 'example6,.txt'))
    thread_three = Thread(target=write_words, args=(200, 'example7.txt'))
    thread_four = Thread(target=write_words, args=(100, 'example8.txt'))

    thread_one.start()
    thread_two.start()
    thread_three.start()
    thread_four.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()
    thread_four.join()

func_write()
thread_write()

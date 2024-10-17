import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name: str, power: int):
        self.knight_name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.knight_name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.knight_name} сражается {days} дней (дня), осталось {enemies} воинов')
        print(f'{self.knight_name} одержал победу сппустя {days} дней (дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

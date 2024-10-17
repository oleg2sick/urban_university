from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        super().__init__()

    def deposit(self):
        for operations in range(100):
            balance_growth = randint(50, 500)
            self.balance += balance_growth
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)
            print(f'Пополнение: {balance_growth}. Баланс: {self.balance}')

    def take(self):
        for operations in range(100):
            balance_decrease = randint(50, 500)
            print(f'Запрос на {balance_decrease}')
            if balance_decrease <= self.balance:
                self.balance -= balance_decrease
                print(f'Снятие: {balance_decrease}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

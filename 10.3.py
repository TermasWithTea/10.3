import threading
import random
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for tran in range(100):
            popol = random.randint(50, 500)
            with self.lock:
                self.balance += popol
                print(f'Пополнение: {popol}. Баланс:{self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for tran in range(100):
            popol = random.randint(50, 100)
            print(f"Запрос на: {popol}")
            with self.lock:
                if popol <= self.balance:
                    self.balance -= popol
                    print(f"Снятие:{popol}. Баланс:{self.balance}")
                else:
                    print(f"Запрос отклонен. Недостаточно средств.")
                    self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2= threading.Thread(target= Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый счет:{bk.balance}")


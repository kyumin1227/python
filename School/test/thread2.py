import threading
from time import sleep

balance = 0

lock = threading.Lock()

def deposit():
    global balance

    for _ in range(20):
        amount = 10
        sleep(0.01)
        new_balance = balance + amount  # 임시 변수로 계산
        sleep(0.01)  # Race condition을 유발할 가능성 증가
        with lock:
            balance = new_balance  # 변경 사항 적용
        print(f"Deposit!, balance : {balance}")

def withdraw():
    global balance

    for _ in range(20):
        amount = 10
        sleep(0.01)
        new_balance = balance - amount  # 임시 변수로 계산
        sleep(0.01)  # Race condition을 유발할 가능성 증가
        with lock:
            balance = new_balance  # 변경 사항 적용
        print(f"Withdraw!, balance : {balance}")

thread_1 = threading.Thread(target=deposit)
thread_2 = threading.Thread(target=withdraw)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"[balance]: {balance}")
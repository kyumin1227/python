# def bar():
#     print("hello")

# def foo(arg_name):
#     arg_name()

# foo(bar)

import threading

# my_lock = threading.Lock()

def bar():
    for count in range(1, 6):
        print(f"bar: {count}")

def foo():
    for count in range(1, 6):
        print(f"foo: {count}")

thread_1 = threading.Thread(target=bar, daemon=True)
thread_2 = threading.Thread(target=foo, daemon=True)

thread_1.start()
thread_2.start()

thread_1.join()    # main_thread가 thread_1의 종료를 기다림
thread_2.join()

print("Finish")

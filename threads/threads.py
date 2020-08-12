import time
import _thread


def do_this(name, delay):
    for i in range(10):
        print(name)
        time.sleep(delay)


try:
    _thread.start_new_thread(do_this, ('Thread 1', 5))
    _thread.start_new_thread(do_this, ('Thread 2', 10))
except Exception as e:
    print(e)
finally:
    print('Multithreading in Python')

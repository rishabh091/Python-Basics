import threading
import time
import _thread

threadLock = threading.Lock()


def do_this(name, delay):
    # acquire lock
    threadLock.acquire()
    # do something
    for i in range(10):
        time.sleep(delay)
        print(name)
    # release lock
    threadLock.release()


try:
    _thread.start_new_thread(do_this, ('Thread 1', 2))
    _thread.start_new_thread(do_this, ('Thread 2', 2))
except Exception as e:
    print(e)


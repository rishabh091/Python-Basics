import threading
import time


def script(thread_name, number):
    print('Thread {} started, name {}'.format(number, thread_name))
    time.sleep(10)
    print('Thread {} finished !!, name {}'.format(number, thread_name))


thread_list = []
for i in range(5):
    name = 'T' + str(i + 1)

    thread = threading.Thread(target=script, args=((i + 1), name))
    thread_list.append(thread)

    thread.start()

print('All thread completed !!')

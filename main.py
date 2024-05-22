import threading
import multiprocessing
import time
from datetime import datetime


def most_usefull_function():
    print('Function is started!')
    time.sleep(5)
    print('Function is ended!')


start_time = datetime.now()
# most_usefull_function()
# most_usefull_function()
# print('delay:', datetime.now() - start_time)


my_thread_1 = threading.Thread(target=most_usefull_function)
my_thread_2 = threading.Thread(target=most_usefull_function)
my_thread_1.start()     #старт певрого потока
my_thread_2.start()     #старт второго потока

my_thread_1.join()  #главный поток должен ждать заверешиня первого потока
my_thread_2.join()  #главный поток должен ждать заверешиня второго потока
print('delay:', datetime.now() - start_time)

import threading
import multiprocessing
import time
from datetime import datetime


# def most_usefull_function():
#     global x
#     print('Function is started!')
#     x += 5
#     time.sleep(5)
#     print('Function is ended!')


# def another_useful_func():
#     # global x
#     x = 5
#     print('Function is started!')
#     x += 5
#     time.sleep(8)
#     print('Function is ended!', x)
#
#
start_time = datetime.now()
# most_usefull_function()
# most_usefull_function()
# print('delay:', datetime.now() - start_time)

# x = 30
# my_thread_1 = threading.Thread(target=most_usefull_function)
# my_thread_2 = threading.Thread(target=most_usefull_function)
# my_thread_1.start()     #старт певрого потока
# my_thread_2.start()     #старт второго потока
#
# my_thread_1.join()  #главный поток должен ждать заверешиня первого потока
# my_thread_2.join()  #главный поток должен ждать заверешиня второго потока
# print('delay:', datetime.now() - start_time, 'x:', x)



# if __name__ == '__main__':
#     x = 5
#
#     my_process_1 = multiprocessing.Process(target=another_useful_func)
#     my_process_2 = multiprocessing.Process(target=another_useful_func)
#
#     my_process_1.start()
#     my_process_2.start()
#
#     my_process_1.join()
#     my_process_2.join()
#
#     print(x)


'''
Задание 1
'''


# A = [1, 2, 3]
# def max_func():
#     print(max(A))
#
#
# def min_func():
#     print(min(A))


# while True:
#     A = []
#     a = int(input("Введите число: "))
#     for i in A:
#         A.append(i)
#     else:
#         break



# my_thread_1 = threading.Thread(target=max_func)
# my_thread_2 = threading.Thread(target=min_func)
# my_thread_1.start()
# my_thread_2.start()
#
# my_thread_1.join()
# my_thread_2.join()

'''
Задание 3
'''
import random


def find_even_numbers(filename):
    with open(filename, 'r') as file:
        with open('even_numbers.txt', 'w') as even_file:
            even_file.write('\n'.join(str([int(i) for i in file.read().split('\n') if int(i) % 2 == 0])))
            print('done1')
            # file.read().split('\n')
    # for i in A:
    #     if i/2 == 0:
    #         A.append(i)
    #     print(A)


def find_odd_numbers(filename):
    with open(filename, 'r') as file:
        with open('odd_numbers.txt', 'w') as odd_file:
            all_str_numbers = file.read().split('\n')
            for num in all_str_numbers:
                if int(num) % 2 == 1:
                    odd_file.write(f'{num}\n')
            # odd_file.write('\n'.join([int(i) for i in file.read().split('\n') if int(i) % 2 == 0]))

# random_numbers = '\n'.join(str[random.randint(-500, 500) for _ in range(10_000)])

with open('nums.txt', 'w') as file:
    file.write("\n".join([str(random.randint(-500, 500)) for _ in range(10_000)]))

with open('nums.txt', 'r') as file:
    A = file.read




user_filename = input('Навзание файла с числами для анализа: ')
t1 = threading.Thread(target=find_even_numbers, args=(user_filename, ))
t2 = threading.Thread(target=find_odd_numbers, args=(user_filename, ))
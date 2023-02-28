# #Вводится количество чисел, затем сами числа, необходимо найти среднее арифметическое четных чисел
# count =int(input("Введите кол-во чисел: ")) #4
# some_list = []
# for i in range(count): #0, 1, 2, 3
#     n = int(input())
#     some_list.append(n)
# print(some_list)

#print([int(input()) for _ in range (int(input("Введите кол-во чисел: ")))])

a = (1, 2, 3, 4,5)

import sys 
import random
# some_list = [0]*10**6
# # some_tuple= tuple(some_list)

# # print(sys.getsizeof(some_list))
# # print(sys.getsizeof(some_tuple))


# some_list = [1, 1, 1,1,1,2]
# print(set(some_list))

# some_list = [random.randint(1,1000) for _ in range(10**6)]
# some_set = {random.randint(1,1000) for _ in range(10**6)}
# print(len(some_list))
# print(len(some_set))




# import time

# some_list = []
# count = 0
# for _ in range(10 ** 6):
#     some_list.append(count)
#     count += 1

# some_set = set()
# count = 0
# for _ in range(10 ** 6):
#     some_set.add(count)
#     count += 1


# find_number = 999998
# start = time.perf_counter()
# print(find_number in some_list)
# end = time.perf_counter()
# a = end - start

# start = time.perf_counter()
# print(find_number in some_set)
# end = time.perf_counter()
# b = end - start
# print(a / b)
# 17. Дан список чисел.\
#       Определите, сколько в нем встречается различных чисел.

some_list = [1, 2,4,6,9,10]
some_set = set(some_list)
print(len(some_list))
Дана последовательность 
из N целых чисел и число K.
 Необходимо сдвинуть 
всю последовательность (сдвиг - циклический) 
на K элементов вправо, 
K – положительное числ

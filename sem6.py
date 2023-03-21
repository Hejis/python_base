some_list = [1, 2, 3, 4, 5, 6, 7]
# for ind in some_list:
#     some_list[ind] = str(some_list[int])
# print(some_list)
new_list = map(str, some_list))
print(new_list)

 ############
def square(n):
        return n ** 2
##############
new_list=map(square, some_list)
 print(new_list)
new_list=map(lambda n: n**2, some_list)
########### 
# Преобразовать список чисел в строчку
print(new_list)

########
    some_list = [1, 2, 3, 4, 5, 6, 7]
    new_list = filter(lambda x: x % 2 == 0, some_list)
    print(new_list)
############################
a = [1,2,3]
b = ['1', '2','3']
print(list(zip(a,b)))
##########
#собрать словарик
en = ['grape', 'apple','banana']
ru = ['виноград', "яблоко", "банан"]
for i, j in zip(en.ru):
    en_ru_dict[i]=j
print(en_ru_dict)

############# можно из списка сделать словарь
number = [10, 225, 123 ,43, 12]
print(list(enumerate(number)))

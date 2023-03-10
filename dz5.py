# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод

# 8-5+2-1
# Вывод
# 4
summ = lambda q,w: q+w
dif=lambda q, w: q-w
stroka = input("Введите строку: ")
result = int(stroka[0])
for i in range(1,len(stroka),2):
    if stroka[i] == "+":
        result = summ(result,int(stroka[i+1]))
    if stroka[i] == "-":
        result = dif(result,int(stroka[i+1]))
print(result)


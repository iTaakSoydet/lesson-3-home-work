# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
n = int(input('Введите колличество элементов - '))
numbers = []
for i in range(n):
    numbers.append(randint(-10, 10))
print(numbers)
numbers2 = []
for i in numbers:
    if i in numbers2:
        continue
    else:
        numbers2.append(i)
print(numbers2)

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите число k - '))
s = []
f = open('file.txt', 'w')
for i in range(k, -1, -1):
    if i > 0:
        a = randint(0, 100)
        if a != 0:
            s.append(f'{a} * x ^ {i} + ')
    elif i == 0:
        a = randint(0, 100)
        if a != 0:
            s.append(f'{a} = 0')
        else:
            s.append('= 0')
f.writelines(s)
f.close()

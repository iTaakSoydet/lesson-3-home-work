# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите число - '))
multipliers = []
for i in range(2, n+1):
    while n % i == 0:
        multipliers.append(i)
        n /= i
print(multipliers)

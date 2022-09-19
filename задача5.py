# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

f = open('file.txt', 'r')
numbers1 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers1.insert(0, i)
print(numbers1)

f = open('file1.txt', 'r')
numbers2 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers2.insert(0, i)
print(numbers2)

result = []
if len(numbers1) > len(numbers2):
    for i in range(1, len(numbers2)):
        if i % 2 == 0:
            result.insert(1, numbers1[i])
        else:
            result.insert(0, numbers1[i] + numbers2[i])
    for i in range(len(numbers2), len(numbers1)):
        result.insert(0, numbers1[i])
elif len(numbers1) < len(numbers2):
    for i in range(1, len(numbers1)):
        if i % 2 == 0:
            result.insert(0, numbers2[i])
        else:
            result.insert(0, numbers2[i] + numbers1[i])
    for i in range(len(numbers1), len(numbers2)):
        result.insert(0, numbers2[i])
else:
    for i in range(1, len(numbers2)):
        if i % 2 == 0:
            result.insert(0, numbers1[i])
        else:
            result.insert(0, numbers1[i] + numbers2[i])

print(result)

s = []
f = open('file2.txt', 'w')
for i in range(0, len(result)):
    if i % 2 == 0:
        s.append(f'{result[i]}')
    else:
        if result[i] == 1:
            s.append(f'*x+')
        else:
            s.append(f'*x^{result[i]}+')
s.append('=0')
f.writelines(s)
f.close()


# def partition(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]

# chunks = list(partition(numbers1, 2))
# print(chunks)

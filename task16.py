# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
n = int(input('Введите размер массива: '))
x = int(input('Введите искомое число от 0 до 9: '))
count = 0
arr = []
for i in range(n):
    arr.append(random.randrange(10))
print(arr)
for i in arr:
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается в массиве {count} раз.')
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


import random
def gen_list(x): 
    in_list = []
    for i in range(x):
        in_list.append(random.randint(0,x))
    return in_list

start = int(input('Введите начало диапазона: ') )
stop = int(input('Введите конец диапазрна: ') )

in_list = gen_list(30)
print(in_list)
idx_list = []


for i in range(len(in_list)):
    if start <= in_list[i] <= stop:
        idx_list.append(i)


print(idx_list)

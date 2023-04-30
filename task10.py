# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Введите кол-во монет: "))
eagle = 0
tails = 0
coin = []
for i in range(n):
    coin.append(random.randrange(0,2))
    if coin[i] != 0:
        eagle += 1
    else:
        tails += 1
print("1-орел, 0-решка")
print(coin)
if eagle > tails:
    print("Переворачиваем решки")
else:
    print("Переворачиваем орлов")
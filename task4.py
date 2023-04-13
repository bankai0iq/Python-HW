# Задача 8: Требуется определить, можно ли от шоколадки размером N x M долек
# отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def inSzChklt(message):
    flag = True
    while flag:
        size = input(message)
        if (not size.isdigit() or int(size) < 1):
            print('Введены не верные данные')
        else:
            flag = False
    return int(size)

n = inSzChklt('Введите длинну шоколадки: ')
m = inSzChklt('Введите ширину шоколадки: ')
k = inSzChklt('Сколько хотите отломить?: ')

if k < n * m:
    if k % n == 0 or k % m == 0:
        print('Получилось')
    else:
        print('Не получилось')

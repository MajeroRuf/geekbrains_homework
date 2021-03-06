"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено."""

from itertools import count, cycle

try:
    a = int(input("Введите целое число начала цикла: "))
    b = int(input("Введите целое число конца цикла: "))
except ValueError as err:
    print('Ошибка', err)
    exit()

my_list =[]
"""Оставлю напоминалку, на лекции сказали count в генератор не пихать :))"""
for el in count(a):
    if el > b:
        break
    else:
        print(el)
        my_list.append(el)
print(my_list)

"""Используем список созданный в первом цикле"""

c = int(input("Введите колличество повторов: "))
d = 0
for el in cycle(my_list):
    if d > c:
        break
    print(el)
    d +=1
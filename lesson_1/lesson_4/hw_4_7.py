"""7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2  * 3 * 4 = 24."""

"""Вот над этим заданием я себе всю голову сломал, хотя вроде бы все понятно,
 но как то тяжело далось"""

def fact_func(fact):
    a = 1
    for i in range(1, fact+1):
        a = a * i
        yield a
fact = 1

try:
    fact = int(input('Введите целое число: '))
except ValueError as err:
    print('Ошибка: ', err)
    exit()

f = 1

for el in fact_func(fact):
    print(f'факториал числа {f}! = {el}')
    f += 1
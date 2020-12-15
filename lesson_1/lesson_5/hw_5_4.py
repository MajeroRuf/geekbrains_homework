"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

"""Создадим функцию замены английского числа на русское"""
def en_ru_func(a):
    b = en_ru.get(a)
    return b

en_ru = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

"""Что то не знаю можно ли по другому затереть файл, при каждом новом заруске,
кроме как взять его на запись и тем самым затереть"""

my_file = open('numeral_rus_hw_5_4.txt', 'w')
my_file.close()

with open('numeral_hw_5_4.txt', 'r') as d_obj:
    for line in d_obj:
        content = line.split(' ')
        a = content[0]
        content = [en_ru_func(a), content[1], content[2]]
        with open('numeral_rus_hw_5_4.txt', 'a') as r_obj:
            r_obj.write(f'{content[0]} - {content[2]}')
"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import sample

"""Сделал вначале просто со строкой уже готовой, но потом решил,
что так не интересно надо нарандомить строку, нарандомить то не сложно оказалось,
но эти кавычки блин, в общем сказалась неопытность"""

with open('numbers_hw_5_5.txt', 'w') as d_obj:
    str_list = [f'{el}' for el in sample(range(1, 100, 5), 10)]
    str_list_new = ' '.join(str_list)
    # str_list = ('10 20 30 40 50 60')
    d_obj.write(str_list_new)


with open('numbers_hw_5_5.txt', 'r') as r_obj:
    s_list = r_obj.read()
    sum_l = sum([int(el) for el in s_list.split(' ')])
    print(sum_l)

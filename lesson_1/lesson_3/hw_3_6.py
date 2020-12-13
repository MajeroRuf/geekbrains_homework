def int_func():
    str_cap = a.capitalize()
    return str_cap

a = str(input('Введите строку: '))
print(int_func())

list_str = "hello my name is konstantin"

str_l = []
str_l = list_str.split(' ')

c = []
for a in str_l:
    c.append(int_func())
print(' '.join(c))





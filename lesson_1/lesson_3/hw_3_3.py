# Вариант без сортировки
def my_func():
    try:
        arg1 = float(input('Введите первый аргумент: '))
        arg2 = float(input('Введите второй аргумент: '))
        arg3 = float(input('Введите третий аргумент: '))
    except ValueError as err:
        print('Ошибкааааааааааа', err)

    a_list =[arg1, arg2, arg3]
    min_el = min(a_list)
    print(min_el)
    a_list.remove(min_el)
    sum_arg = sum(a_list)
    return sum_arg

sum_arg2 = my_func()
print(sum_arg2)

#Вариант с сортировкой
def my_func():
    try:
        arg1 = float(input('Введите первый аргумент: '))
        arg2 = float(input('Введите второй аргумент: '))
        arg3 = float(input('Введите третий аргумент: '))
    except ValueError as err:
        print('Error', err)

    a_list =[arg1, arg2, arg3]
    a_list.sort()
    sum_arg = a_list[1] + a_list[2]
    return sum_arg

sum_arg2 = my_func()
print(sum_arg2)
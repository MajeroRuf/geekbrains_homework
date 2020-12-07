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
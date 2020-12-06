def division_func(arg_1, arg_2):
    return arg_1/arg_2
arg_1 = float(input('введите аргумент 1: '))
arg_2 = float(input('Введите аргусент 2: '))

try:
    print(division_func(arg_1, arg_2))
except ZeroDivisionError as err:
    print('Error!!!', err)


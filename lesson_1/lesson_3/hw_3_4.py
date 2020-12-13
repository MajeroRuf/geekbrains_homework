# С оператором **
def my_func():
    try:
        arg_1 = float(input('Ведите положительное число: '))
        arg_2 = int(input('Введите отрицательную степень: '))
    except ValueError as err:
        print('Error', err)

    step = arg_1**arg_2
    return step

result = my_func()
print(result)

#Без оператора **
def my_func():
    try:
        arg_1 = float(input('Ведите положительное число: '))
        arg_2 = int(input('Введите отрицательную степень: '))
    except ValueError as err:
        print('Error', err)
    if arg_2 < 0:
        i = -1
        a = arg_1
        while i > arg_2:
            a = a * arg_1
            i -=1
        step = 1/(a)
    else:
        print('Степень не отрицательная!!!')
    return step
result = my_func()
print(result)



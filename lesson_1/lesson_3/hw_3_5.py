def sum_func(a):
    list_str = a.split(' ')
    list_int = []
    for i in list_str:
        if i == 's':
            global exit_cycle
            """Долго думал как можно выйти из условия и цикла, 
            но в голову пришла только идея с глобальной переменной"""
            exit_cycle = i
            print('Подсчет окончен')
            break
        else:
            i = float(i)
            list_int.append(i)
    return list_int

exit_cycle = ()
b = 0

while exit_cycle !='s':
    a = str(input("Введите строку чисел разделенную пробелом,"
                  " если захотите закончить ввод введите букву s : "))
    exit_cycle = a
    b = (sum(sum_func(a)) + b)
    print(b)





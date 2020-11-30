proceed = float(input("Введите значение выручки фирмы: "))
costs = float(input("Введите значение издержек фирмы: "))
result = proceed - costs
if result > 0:
    print("Прибыль вашей фирмы составляет: {} у.е".format(round(result, 2)))
    profit = result / costs * 100
    print("Ренатабельность Вашей фирмы составляет: {}%".format(round(profit, 2)))
    num_emp = int(input("Введите численность сотрудников:"))
    profit_emp = result / num_emp
    print("Прибыль вашей фирмы в расчете на одного сотрудника составляет: {} у.е".format(round(profit_emp, 2)))
elif result < 0:
    print("Убыток вашей фирмы составляет: {} у.е".format(round(result, 2)))
elif result == 0:
    print("Ваша фирма работает в ноль")
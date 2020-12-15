"""7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json
firm_profit = 0
quantity = 0
sum_profit = 0
average_profit = 0
firm_profit_dict = {}
firm_loss_dict = {}

with open('firm.txt', encoding='utf-8') as d_obj:
    for line in d_obj:
        firm_list = line.split(' ')
        try:
            firm_profit = int(firm_list[2]) - int(firm_list[3])
        except ValueError as err:
            print("Error", err)
        if firm_profit >= 0:
            sum_profit = sum_profit + firm_profit
            firm_profit_dict.update({firm_list[0]:firm_profit})
            quantity = quantity + 1
        else:
            firm_loss_dict.update({firm_list[0]:firm_profit})
    try:
        average_profit = sum_profit / quantity
        average_profit_dict = {'average_profit':average_profit}
    except Exception as err:
        print('Error', err)
    final_list = [firm_profit_dict, average_profit_dict]
with open('final_firm.json', 'w') as j_obj:
    json.dump(final_list, j_obj)


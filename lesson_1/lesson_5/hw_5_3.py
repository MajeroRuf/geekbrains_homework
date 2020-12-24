"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('emp_sal_hw_5_3.txt', 'r') as d_obj:
    sum_sal = 0
    quantity_emp = 0
    income = 0

    for line in d_obj:
        content = line.split(',')
        try:
            sum_sal = sum_sal + int(content[1])
        except ValueError as err:
            print('Error', err)
            exit()
        quantity_emp += 1
        if int(content[1]) < 20000:
            print(f'Данный сотрудник имеет оклад менее 20000 руб: {content[0]}')

    income = sum_sal / quantity_emp
    print(f'Средняя величина дохода сотрудников: {income} руб.')

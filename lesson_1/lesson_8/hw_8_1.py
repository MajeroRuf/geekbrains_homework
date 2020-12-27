"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных."""

class MyException(Exception):
    def __init__(self, text):
        self.text = text

class Date:
    months_l = [1, 3, 5, 7, 8, 10, 12]
    months_s = [4, 6, 9, 11]

    def __init__(self, day):
        self.day = day


    @staticmethod
    def valid_date(day: str):
        dmy = Date.int_date(day)

        if dmy[1] in Date.months_l and dmy[0] > 31:
            raise ("Не верный день 1")
        if dmy[1] in Date.months_s and dmy[0] > 30:
            raise ("Не верный день 2")
        if dmy[2] % 4 == 0 and dmy[1] == 2 and dmy[0] > 29:
            raise ('Не верный день Февраля 1')
        if dmy[2] % 4 != 0 and dmy[1] == 2 and dmy[0] > 28:
            raise ('Не верный день Февраля 2')
        if not (0 < dmy[1] < 13):
            raise ('Не верный месяц')
        return True


    @classmethod
    def int_date(cls, day: str):
        dmy_s = day.split('-')
        dmy = [int(el) for el in dmy_s]
        return dmy

date_1 = Date.valid_date('22-11-2020')
date_2 = Date.valid_date('31-11-2020')
date_3 = Date.valid_date('30-02-2020')
date_4 = Date.valid_date('29-02-2019')
date_5 = Date.valid_date('30-13-2020')

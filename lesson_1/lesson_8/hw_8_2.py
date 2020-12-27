"""2. Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой."""

class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]

def my_exp(a, b):
    if not b:
        raise MyException('Деление на 0!!!', [1, 2, 3])
    return a / b

try:
    my_exp(1, 0)
except Exception as err:
    print(type(err), err)

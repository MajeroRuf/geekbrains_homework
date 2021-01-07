"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
— первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""

import random
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f' {self.matrix}'

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)

try:
    x = int(input("Введите первый индекс матрицы: "))
    y = int(input("Введите второй индекс марицы: "))
except ValueError as err:
    print('Число не целое', err)

matrix1 = Matrix([[random.randint(0, 100) for i in range(x)] for j in range(y)])
print(f'первая матрица: {matrix1}')
matrix2 = Matrix([[random.randint(0, 100) for i in range(x)] for j in range(y)])
print(f'вторая матрица: {matrix2}')
matrix3 = Matrix([[random.randint(0, 100) for i in range(x)] for j in range(y)])
print(f'третья матрица: {matrix3}')
matrix4 = matrix1 + matrix2 + matrix3
print(f'сумма матриц:   {matrix1}')



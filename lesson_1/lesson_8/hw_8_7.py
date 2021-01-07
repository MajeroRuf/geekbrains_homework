"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""

"""Пришлось искать в интернете, что такое комплексные числа и как решаются уравнения с ними"""
class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + ({self.b +other.b}i)'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - self.b * other.b} + ({self.a * other.b + self.b * other.a}i)'

c_1 = ComplexNumbers(-4, -8)
c_2 = ComplexNumbers(6, -11)
print(c_1 + c_2)
print(c_1 * c_2)
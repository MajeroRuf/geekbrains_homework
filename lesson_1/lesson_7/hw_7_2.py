"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @property
    def sum_cloth(self):
        return f'Всего ткани затраченой на пошив: {(self.size/6.5 + 0.5) + (2 * self.growth + 0.3): .2f} м'

    @abstractmethod
    def abs_metod(self):
        pass

class Coat(Clothes):

    def cons_coat(self):
        return f'На пальто нужно: {self.size/6.5 + 0.5: .2f} м ткани'


    def abs_metod(self):
        pass

class Costume(Clothes):

    def cons_costume(self):
        return f'На костюм нужно: {2 * self.growth + 0.3: .2f} м ткани'


    def abs_metod(self):
        pass


coat = Coat(50, 10)
costume = Costume(50, 10)


print(coat.cons_coat())
print(costume.cons_costume())
print(coat.sum_cloth)




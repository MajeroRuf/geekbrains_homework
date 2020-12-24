"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат"""

"""Получился маленьний текстовый квест ))))"""

from time import sleep

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police
    def go(self):
        print(f'Машина {self.color} {self.name} поехала со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась')

    def show_speed(self):
        print(f'Машина {self.color} {self.name} едет со скоростью {self.speed} км/ч')

    def turn(self):
        print(f'Машина {self.color} {self.name} едет Налево -- Направо -- Налево')

    def fine(self):
        print('Вас оштрафовали')

    def chase(self):
        print(f'Машина {self.color} {self.name} оторвалась от погони на скорости {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        print(f'Машина {self.color} {self.name} едет со скоростью {self.speed} км/ч')
        if int(self.speed) > 60:
            print('Вы превышаете скорость')

class SportCar(Car):
    def show_speed(self):
        print(f'Машина {self.color} {self.name} едет со скоростью {self.speed} км/ч')
        if int(self.speed) > 60:
            print('Вы превышаете скорость')


class WorkCar(Car):
    def show_speed(self):
        print(f'Машина {self.color} {self.name} едет со скоростью {self.speed} км/ч')
        if int(self.speed) > 40:
            print(f'Машина {self.color} {self.name} сдохла')
            exit()

class PoliceCar(Car):
    def flesher(self):
        print(f'Включились мигалки и сирена')

    def go(self):
        print(f'Полицейская машина {self.color} {self.name} поехала со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'Полицейская машина {self.color} {self.name} остановилась')

    def turn(self):
        print(f'Полицейская машина {self.color} {self.name} едет Налево -- Направо -- Направо')
try:
    m = int(input('Выберите номер машины 1-TownCar, 2-SportCar, 3-WorkCar: '))
except ValueError as err:
    print('Error', err)

if m == 1:
    car = TownCar(10, 'Белая', 'Kia', False)
elif m == 2:
    car = SportCar(50, 'Красный', 'Форд Мустанг', False)
elif m == 3:
    car = WorkCar(10, 'Желтый', "Кран", False)

policecar1 = PoliceCar(40, 'голубая', 'BMW', True)

car.go()
sleep(1)
try:
    s = int(input('Введите скорость машины: '))
except ValueError as err:
    print('Error, err')
car.speed = s
sleep(1)
car.show_speed()
sleep(1)
if car.speed > 60 and car.speed < 170:
   sleep(1)
   policecar1.go()
   policecar1.flesher()
   sleep(1)
   car.stop()
   sleep(1)
   policecar1.stop()
   sleep(1)
   car.fine()
elif car.speed >= 170:
    sleep(1)
    policecar1.go()
    policecar1.flesher()
    sleep(1)
    car.turn()
    sleep(1)
    policecar1.turn()
    sleep(1)
    policecar1.stop()
    sleep(1)
    car.chase()


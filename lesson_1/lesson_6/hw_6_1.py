"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт. """

from time import sleep

class TrafficLight:
    def __init__(self, _color):
        self.color = _color

    def running(self):
        print("Светафор работает")

tl1 = TrafficLight('Red')
tl1.running()
while True:
    tl1 = TrafficLight('Red')
    print(tl1.color)
    sleep(7)
    tl1 = TrafficLight('Yellow')
    print(tl1.color)
    sleep(2)
    tl1 = TrafficLight('Green')
    print(tl1.color)
    sleep(3)





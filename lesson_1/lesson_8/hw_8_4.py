"""Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП."""

"""Идея была такова, что мы всегда можем вывести наш склад на экран, соответственно мы знаем ID нужного нам устройства
и по нему производить манитуляции с техникой переместить в оффис или на склад, а так же добавлять и удалить. 
Над заданием работал дня 4, при этом первые дня 2 знатно тупил, толком не мог поставить для себя задачу
и сформулировать приоритеты. Тут надо сказать спасибо Агате именно ее решение заставило меня собраться с мыслями, 
но копировать неинтересно, да и не мой уровень там, поэтому пришлось напрячься. Главный прогресс пошел, 
когда я все же вспомнил, что работаю с базами данных, а какая база без уникальных ID, отбор всего стал проще. 
Конечно осталось еще много недоработок и идей, например тот же ID, про который я писал выше никак не должен
создаваться пользователем, процесс создания и прикрепления должен быть автоматизирован, да и упростить многое можно,
но времени и сил больше не осталось, так что пусть пока будет так. Может когда выросту вернусь к задаче,
да и сама задача как таковая, может найти свое применение. Закончил 29.12.2020 в 01:12"""


class WareHouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Office:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class WareHouse_store:

    """Создаем метод учета техники на складе"""
    @staticmethod
    def list(officeequipment: 'OfficeEquipment', printer: 'Printer', scanner: 'Scanner', xerox: 'Xerox'):
        o_store = f'Всего  у фирмы: {officeequipment.cnt_office_equipment} единиц техники\n' \
                  f'из них: \n' \
                  f'Принтеров: {printer.cnt_printer} шт.\n' \
                  f'Сканеров: {scanner.cnt_scanner} шт.\n' \
                  f'Ксероксов: {xerox.cnt_xerox} шт.\n'
        return o_store

    """Создаем счетчики склада"""
    @staticmethod
    def list_wh(store: 'WareHouse'):
        cnt_w = 0
        cnt_w_printer = 0
        cnt_w_scanner = 0
        cnt_w_xerox = 0
        for el in office_equ:
            if el.storage.name == 'Склад_1' and el.equipment_name == 'Printer':
                cnt_w += 1
                cnt_w_printer += 1
            elif el.storage.name == 'Склад_1' and el.equipment_name == 'Scanner':
                cnt_w += 1
                cnt_w_scanner += 1
            elif el.storage.name == 'Склад_1' and el.equipment_name == 'Xerox':
                cnt_w += 1
                cnt_w_xerox += 1

        wh_store = f'На складе {store.name} находящегося по адресу {store.address} находится \n' \
                             f'{cnt_w} единиц техники.\n' \
                             f'из них: \n' \
                             f'Принтеров: {cnt_w_printer} шт.\n' \
                             f'Сканеров: {cnt_w_scanner} шт.\n' \
                             f'Ксероксов: {cnt_w_xerox} шт.\n'
        return wh_store

    """Создаем счетчики офиса"""
    @staticmethod
    def list_o(store: 'Office'):
        cnt_o = 0
        cnt_o_printer = 0
        cnt_o_scanner = 0
        cnt_o_xerox = 0
        for el in office_equ:
            if el.storage.name == 'Офис_1' and el.equipment_name == 'Printer':
                cnt_o += 1
                cnt_o_printer += 1
            elif el.storage.name == 'Офис_1' and el.equipment_name == 'Scanner':
                cnt_o += 1
                cnt_o_scanner += 1
            elif el.storage.name == 'Офис_1' and el.equipment_name == 'Xerox':
                cnt_o += 1
                cnt_o_xerox += 1

        off_store = f'В {store.name} находящегося по адресу {store.address} находится \n' \
                             f'{cnt_o} единиц техники.\n' \
                             f'из них: \n' \
                             f'Принтеров: {cnt_o_printer} шт.\n' \
                             f'Сканеров: {cnt_o_scanner} шт.\n' \
                             f'Ксероксов: {cnt_o_xerox} шт.\n'
        return off_store

    """Метод передачи техники со склада в офис  по его ID"""

    @staticmethod
    def give_office(id_e):
        for el in office_equ:
            if el.id_e == id_e:
                el.storage = office
                office_equ.append(el)
                office_equ.remove(el)
                return f'Перемещаем устройство с ID {id_e} со склада в офис'

    """Метод передачи техники из офиса на склад  по его ID"""

    @staticmethod
    def return_warehouse(id_e):
        for el in office_equ:
            if el.id_e == id_e:
                el.storage = warehouse
                office_equ.append(el)
                office_equ.remove(el)
                return f'Перемещаем устройство с ID {id_e} из офиса на склад'

    """Метод уничтожения устройства по его ID"""

    @staticmethod
    def remove_officeequipment(id_e):
        for el in office_equ:
            if el.id_e == id_e:
                if el.equipment_name == 'Printer':
                    Printer.cnt_printer -= 1
                elif el.equipment_name == 'Scanner':
                    Scanner.cnt_scanner -=1
                elif el.equipment_name == 'Xerox':
                    Xerox.cnt_xerox -=1
                office_equ.remove(el)
                OfficeEquipment.cnt_office_equipment -=1
                return f'Уничтожаем устройство с ID {id_e}'

    """Далее методы добавления устройст"""

    @staticmethod
    def addofficeequipment():
        office_type = input('Ввод: ')
        return office_type

    @staticmethod
    def addprinter(wh: 'WareHouse'):
        firm_p_name = input('Введите название фирмы производителя: ')
        model_p_name = input("Введите название модели: ")
        try:
            price = float(input('Введите цену: '))
            id_p_add = int(input('Введите уникальный целочисленный ID устройства: '))
            speed_copy = int(input('Введите целочисленную скорость копирования принтера: '))
        except ValueError as err:
            print('Ошибка ввода данных', err)
        return Printer(price, firm_p_name, model_p_name, id_p_add, speed_copy, wh)

    @staticmethod
    def addscanner(wh: 'WareHouse'):
        firm_s_name = input('Введите название фирмы производителя: ')
        model_s_name = input("Введите название модели: ")
        try:
            price = float(input('Введите цену: '))
            id_s_add = int(input('Введите уникальный целочисленный ID устройства: '))
            quick_scan = bool(input('Введите 1 если у сканера есть быстрое сканироание, 0 если нет: '))
        except ValueError as err:
            print('Ошибка ввода данных', err)
        return Scanner(price, firm_s_name, model_s_name, id_s_add, quick_scan, wh)


    @staticmethod
    def addxerox(wh: 'WareHouse'):
        firm_x_name = input('Введите название фирмы производителя: ')
        model_x_name = input("Введите название модели: ")
        try:
            price = float(input('Введите цену: '))
            id_x_add = int(input('Введите уникальный целочисленный ID устройства: '))
            double_sided = bool(input('Введите 1 если у ксерокса есть двусторонняя печать, 0 если нет: '))
        except ValueError as err:
            print('Ошибка ввода данных', err)
        return Xerox(price, firm_x_name, model_x_name, id_x_add, double_sided, wh)


"""Создание классов техники"""

class OfficeEquipment:
    cnt_office_equipment = 0
    def __init__(self, equipment_name, price, name_firm, name_model, id_e, storage: 'WareHouse'):
        self.equipment_name = equipment_name
        self.storage = storage
        self.price = price
        self.name_firm = name_firm
        self.name_model = name_model
        self.id_e = id_e
        OfficeEquipment.cnt_office_equipment +=1


    def __str__(self):
        text = ''
        for key in self.__dict__:
            if key == 'storage':
                text = f"{text}{key} : {self.__dict__[key].name} \n"
            else:
                text = f"{text}{key} : {self.__dict__[key]} \n"
        return text


class Printer(OfficeEquipment):
    cnt_printer = 0
    def __init__(self, price: float, name_firm, name_model, id_e, copy_speed, store):
        super().__init__('Printer', price, name_firm, name_model, id_e, store)
        self.copy_speed = copy_speed
        Printer.cnt_printer +=1


class Scanner(OfficeEquipment):
    cnt_scanner = 0
    def __init__(self, price: float, name_firm, name_model, id_e, quick_scan, store):
        super().__init__('Scanner', price, name_firm, name_model, id_e, store)
        self.quick_scan = quick_scan
        Scanner.cnt_scanner +=1

class Xerox(OfficeEquipment):
    cnt_xerox = 0
    def __init__(self, price: float, name_firm, name_model, id_e, double_sided, store):
        super().__init__('Xerox', price, name_firm, name_model, id_e ,store)
        self.double_sided = double_sided
        Xerox.cnt_xerox +=1


"""Создание экземпляров складов, техники и наполнение склада"""

if __name__ == "__main__":
    warehouse = WareHouse('Склад_1', 'Москва ул. Кибальчича д.10')
    office = Office('Офис_1', 'Калуга ул. Кубяка д.3')

    office_equ = [Printer(25000.0, 'HP', 'LJ-2090', 1000, 20, warehouse),
               Scanner(5000.0, 'Canon', 'LiDE400', 2000, True, warehouse),
               Xerox(3000.0, 'Xerox', 'B205', 3000, True, office),
               Xerox(2500.0, 'Samsung', 'PS40', 3001, False, warehouse),
               Printer(25000.0, 'HP', 'LJ-2090', 1001, 20, office),
               Printer(35000.0, 'LG', 'nm-1030', 1002, 30, warehouse)]


    """Добавление техники на склад, выбор между офисом и складом делать не стал, все на склад"""

    while True:
        print("введите наименование техники в виде Printer, Scanner, Xerox или stop для окончания ввода: ")
        o_tech = WareHouse_store.addofficeequipment()
        if o_tech == 'Printer':
            print('Введите параметры принтера')
            p_tech = WareHouse_store.addprinter(warehouse)
            office_equ.append(p_tech)
        elif o_tech == 'Scanner':
            print('Введите параметры сканера')
            p_tech = WareHouse_store.addscanner(warehouse)
            office_equ.append(p_tech)
        elif o_tech == 'Xerox':
            print('Введите параметры Ксерокса')
            p_tech = WareHouse_store.addxerox(warehouse)
            office_equ.append(p_tech)
        elif o_tech == 'stop':
            break

    """Все дальше поехали многочисленные проверки всех методов, поэтому много повторов вызовов"""

    for i in office_equ:
        print(i)

    print(WareHouse_store.list(OfficeEquipment, Printer, Scanner, Xerox))


    print(WareHouse_store.list_wh(warehouse))
    print(WareHouse_store.list_o(office))

    print(WareHouse_store.give_office(1000))

    for i in office_equ:
        print(i)

    print(WareHouse_store.list(OfficeEquipment, Printer, Scanner, Xerox))

    print(WareHouse_store.list_o(office))
    print(WareHouse_store.list_wh(warehouse))

    print(WareHouse_store.return_warehouse(3000))

    print(WareHouse_store.list_o(office))
    print(WareHouse_store.list_wh(warehouse))

    print(WareHouse_store.remove_officeequipment(1002))

    print(WareHouse_store.list_o(office))
    print(WareHouse_store.list_wh(warehouse))

    for i in office_equ:
        print(i)

    print(WareHouse_store.list(OfficeEquipment, Printer, Scanner, Xerox))
    print(WareHouse_store.list_o(office))
    print(WareHouse_store.list_wh(warehouse))



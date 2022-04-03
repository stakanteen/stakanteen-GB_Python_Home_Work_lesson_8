# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(
            self,
            name_warehouse: str,
            max_places: int,
            responsible: str
                 ):
        self.name_warehouse = name_warehouse
        self.max_places = max_places
        self.free_places = max_places
        self.responsible = responsible

    def input_items(self, quantity: int):
        if quantity < 0:
            print(f'Количество должно быть положительным числом. '
                  f'Состояние склада не изменилось. Свободно {self.free_places} мест')
        elif quantity > self.free_places:
            print(f'Нельзя добавить столько единиц техники. Доступно {self.free_places} мест')
        else:
            self.free_places = self.free_places - quantity
            print(f"На склад {self.name_warehouse} добавлено {quantity} единиц техники. Осталось {self.free_places} мест")

    def output_utems(self, quantity: int):
        if quantity < 0:
            print(f'Количество должно быть положительным числом. '
                  f'Состояние склада не изменилось. Свободно {self.free_places} мест')
        elif quantity > (self.free_places - self.max_places)*-1:
            print(f'Нельзя забрать столько единиц техники. '
                  f'Доступно {(self.free_places - self.max_places)*-1} единиц')
        else:
            self.free_places = self.free_places + quantity
            print(f"Со склада {self.name_warehouse} забрано {quantity} единиц техники. Осталось {self.free_places} мест")

class OfficeEquipment:

    def __init__(
            self,
            equipment_type: str,
            inventory_number: int,
            size: str
    ):
        self.equipment_type = equipment_type
        self.inventory_number = inventory_number
        self.size = size

class Printer(OfficeEquipment):

    def __init__(
            self,
            color_mode: str,
    ):
        self.color_mode = color_mode

class Scanner(OfficeEquipment):
    def __init__(
            self,
            scan_speed: int
    ):
        self.scan_speed = scan_speed

class Xerox(OfficeEquipment):
    def __init__(
            self,
            scan_option: bool
    ):
        self.scan_option = scan_option

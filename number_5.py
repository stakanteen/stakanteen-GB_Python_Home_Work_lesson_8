# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

class Warehouse:
    def __init__(
            self,
            name_warehouse: str,
            max_places: int,
    ):
        self.name_warehouse = name_warehouse
        self.existing_equipment = {
            'printers': [],
            'scanners': [],
            'xeroxes': []
        }
        self.max_places = max_places
        self.free_places = max_places
        self.output_equipment = {}

    def input_items(self, equipment):
        if self.free_places == 0:
            print(f'Нельзя добавить технику. Мест на складе нет')
        else:
            if isinstance(equipment, Printer):
                if equipment.inventory_number not in self.existing_equipment['printers']:
                    self.existing_equipment['printers'].append(equipment.inventory_number)
                    self.free_places -= 1
                    print(f"На склад {self.name_warehouse} добавлен принтер {equipment.inventory_number}. "
                          f"Осталось {self.free_places} мест")
                else:
                    print(f'Принтер уже числится на складе. Осталось {self.free_places} мест')
            elif isinstance(equipment, Scanner):
                if equipment.inventory_number not in self.existing_equipment['scanners']:
                    self.existing_equipment['scanners'].append(equipment.inventory_number)
                    self.free_places -= 1
                    print(f"На склад {self.name_warehouse} добавлен сканер {equipment.inventory_number}. "
                          f"Осталось {self.free_places} мест")
                else:
                    print(f'Сканнер уже числится на складе. Осталось {self.free_places} мест')
            elif isinstance(equipment, Xerox):
                if equipment.inventory_number not in self.existing_equipment['xeroxes']:
                    self.existing_equipment['xeroxes'].append(equipment.inventory_number)
                    self.free_places -= 1
                    print(f"На склад {self.name_warehouse} добавлен ксерокс {equipment.inventory_number}. "
                          f"Осталось {self.free_places} мест")
                else:
                    print(f'Ксерокс уже числится на складе. Осталось {self.free_places} мест')

    def output_items(self, equipment, ouput_department):
        if isinstance(equipment, Printer):
            if equipment.inventory_number in self.existing_equipment['printers']:
                self.existing_equipment['printers'].remove(equipment.inventory_number)
                self.free_places += 1
                self.output_equipment[equipment.inventory_number] = ouput_department
                print(f'Принтер {equipment.inventory_number} был передан в отдел {ouput_department}. '
                      f'На складе {self.name_warehouse} доступно {self.free_places} мест')
            else:
                print('Такой техники нет на складе!')
        elif isinstance(equipment, Scanner):
            if equipment.inventory_number in self.existing_equipment['scanners']:
                self.existing_equipment['scanners'].remove(equipment.inventory_number)
                self.free_places += 1
                self.output_equipment[equipment.inventory_number] = ouput_department
                print(f'Принтер {equipment.inventory_number} был передан в отдел {ouput_department}. '
                      f'На складе {self.name_warehouse} доступно {self.free_places} мест')
            else:
                print('Такой техники нет на складе!')
        elif isinstance(equipment, Xerox):
            if equipment.inventory_number in self.existing_equipment['xeroxes']:
                self.existing_equipment['xeroxes'].remove(equipment.inventory_number)
                self.free_places += 1
                self.output_equipment[equipment.inventory_number] = ouput_department
                print(f'Принтер {equipment.inventory_number} был передан в отдел {ouput_department}. '
                      f'На складе {self.name_warehouse} доступно {self.free_places} мест')
            else:
                print('Такой техники нет на складе!')

class OfficeEquipment:

    def __init__(self, inventory_number: int):
        self.inventory_number = inventory_number


class Printer(OfficeEquipment):

    def __init__(self, color_mode: bool, inventory_number):
        super().__init__(inventory_number)
        self.color_mode = color_mode


class Scanner(OfficeEquipment):

    def __init__(self, scan_speed: int, inventory_number):
        super().__init__(inventory_number)
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):

    def __init__(self, scan_option: bool, inventory_number):
        super().__init__(inventory_number)
        self.scan_option = scan_option


printer1 = Printer(color_mode=True, inventory_number=24432)
scanner1 = Scanner(scan_speed=5, inventory_number=54546)
xerox1 = Xerox(scan_option=True, inventory_number=889900)
printer2 = Printer(color_mode=True, inventory_number=12345)
scanner2 = Scanner(scan_speed=5, inventory_number=34567)
xerox2 = Xerox(scan_option=True, inventory_number=23456)
printer3 = Printer(color_mode=False, inventory_number=555555)
wh1 = Warehouse('wh1', 10)

print('Добавляем принтер')
wh1.input_items(equipment=printer1)
print(' ')
print('Попытка добавить ту же аппаратуру:')
wh1.input_items(equipment=printer1)
print(' ')
print('Текущее оборудование на складе:')
print(wh1.existing_equipment)
print(' ')
print(' ')
print('Добавляем сканер')
wh1.input_items(equipment=scanner1)
print(' ')
print('Попытка добавить ту же аппаратуру:')
wh1.input_items(equipment=scanner1)
print(' ')
print('Текущее оборудование на складе:')
print(wh1.existing_equipment)
print(' ')
print(' ')
print('Добавляем Ксерокс')
wh1.input_items(equipment=xerox1)
print(' ')
print('Попытка добавить ту же аппаратуру:')
wh1.input_items(equipment=xerox1)
print(' ')
print('Текущее оборудование на складе:')
print(wh1.existing_equipment)
print(' ')
print('Повторим операции и добавим еще принтер, сканнер и ксерокс')
wh1.input_items(equipment=printer2)
wh1.input_items(equipment=scanner2)
wh1.input_items(equipment=xerox2)
print(' ')
print('Текущее оборудование на складе:')
print(wh1.existing_equipment)
print(' ')
print('Заберем о склада принтер и сканер: ')
wh1.output_items(equipment=printer1, ouput_department='Finance')
wh1.output_items(equipment=scanner1, ouput_department='HR')
print(' ')
print('Текущее оборудование на складе:')
print(wh1.existing_equipment)
print(' ')
print('Учет движения техники:')
print(wh1.output_equipment)
print(' ')
print('Попробуем убрать принтер, который не был заведен на склад: ')
wh1.output_items(equipment=printer3, ouput_department='GR')
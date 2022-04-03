# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime
import re

class Data:

    @classmethod #через datetime уже есть проверка на валидность даты
    def date_like_number_datetime(cls, input_string: str):
        try:
            result = int(datetime.datetime.strptime(input_string, '%d-%m-%Y').strftime('%d%m%Y'))
        except ValueError:
            result = 'Такой даты нет'
        return result

    @classmethod
    def date_like_number(cls, input_string: str):
        d = int(input_string[0:2])
        m = int(input_string[3:5])
        y = int(input_string[-4:])
        dmy = int(input_string[0:2] + input_string[3:5] + input_string[-4:])
        return dmy

    @staticmethod
    def check_date(input_string: str):
        result = 'Что-то пошло не так'
        day = int(input_string[0:2])
        month = int(input_string[3:5])
        year = int(input_string[-4:])
        month_31 = [1, 3, 5, 7, 8, 10, 12]
        month_30 = [4, 6, 9, 11]
        month_28_29 = [2]
        leap_year = [i for i in range(0, 3000) if i % 4 == 0]
        if year > 0:
            if year in leap_year and month in month_28_29:
                if 0 > day or day > 28:
                    result = 'Столько дней в феврале високосного года не бывает!'
                else:
                    result = 'Такая дата существует'
            elif year not in leap_year and month in month_28_29:
                if 0 > day or day > 29:
                    result = 'Столько дней в феврале невисокосного года не бывает!'
                else:
                    result = 'Такая дата существует'
            elif month in month_30:
                if 0 > day or day > 30:
                    result = 'Столько дней в этом месяце быть не может'
                else:
                    result = 'Такая дата существует'
            elif month in month_31:
                if 0 > day or day > 31:
                    result = 'Столько дней в этом месяце быть не может'
                else:
                    result = 'Такая дата существует'
        else:
            result = 'Да кто его знает, что там было до нашей эры'
        return result


date = '28-05-2024'
print('Result:', Data.date_like_number_datetime(date), 'Type:', type(Data.date_like_number_datetime(date)))
print('Result:', Data.date_like_number(date), 'Type:', type(Data.date_like_number(date)))
print(Data.check_date(date))

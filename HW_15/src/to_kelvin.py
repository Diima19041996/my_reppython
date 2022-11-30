"""
Этот модуль конвертирует Фарингейты в Кельвины
"""
from prettytable import PrettyTable

def kelvin(fahrenheit: int) -> str:
    """
    Конвертирует Фарингейты в Кельвины
    :param fahrenheit: значение в градусах по Фарингейту
    :return: текстовая таблица со значениями в Фарингейтах и кельвинах
    """
    kelvin_value = 5. / 9. * (fahrenheit - 32) + 273.15

    table = PrettyTable(['Фаренгейтах', 'Кельвинах'])
    table.add_row([fahrenheit, kelvin_value])

    # return table.get_string()
    print(table.get_string())


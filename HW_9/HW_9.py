# Задание:
# 1- Создаем класс
# 2- Добавляем класс метод
# 3- Добавляем статический метод.
class Vector:
    """
    Создаем класс
    """
    min_coord = 0
    max_coord = 100

    """
    Добавляем класс метод определяющий диапазон значений
    """

    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    """
    Создание метода с прверкой корректности вносимых пользователем значений
    """

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    """
    Создаем статитечский метот вычисляющий сумму переменных
    """

    @staticmethod
    def sum(x, y):
        return x+y

v = Vector(1, 2)
# print(Vector.validate(5))
# res = Vector.get_coord(v)
# print(res)
print(Vector.sum(5, 6))


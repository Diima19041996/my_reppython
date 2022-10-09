# Легкий вариант д\з 1-ое задание "Создать класс"
class Car():
    """ Описание автомобиля """
    def __init__(self, brand, engine):
        """ Свойства автомобиля """
        self.brand = brand
        self.engine = engine

    def name_car(self):
        """ Демонстрация общих характеристик """
        print(self.brand + ' ' + str(self.engine))



# 2-ое задание: " Создание дочернего класса "NewCar", 3-е задание: переназначение метода "name_car" родительского класса"

class NewCar(Car):
    """ Описание свойств нового автомобиля  """
    def __init__(self, brand, engine, price):
        super().__init__(brand, engine)
        self.price = price

    def name_car(self):
            """ Демонстрация общих характеристик """
            print(self.brand + ' ' + str(self.engine) + ' ' + str(self.price))

my_car = NewCar('BMW', 3.0, 2000)
my_car.name_car()













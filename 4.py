#-*- coding: utf- 8 -*-
# присваивание переменным значений:
# всего авто
cars = 100
# мест в авто
space_in_a_car = 4.0
# всего водителей
drivers = 30
# всего пассажиров
passangers = 90
#вычисления с использованием переменных:
# авто без водителей
cars_not_driven = cars - drivers
# в каждом авто по шефу
cars_driven = drivers
# посчитаем вместимость, хоть она и не понадобится далее
carpool_capacity = cars_driven * space_in_a_car
# разбиваем пассажиров по машинам
average_passengers_per_car = passangers / cars_driven

# красивый вывод
print u"В наличии", cars, u"автомобилей."
print u"И только", drivers, u"водителей вышли на работу."
print u"Получается что", cars_not_driven, u"человек."
print u"Сегодня нужно отвезти", passangers, u"человек."
print u"В каждой машине будет примерно", average_passengers_per_car, u"человека."
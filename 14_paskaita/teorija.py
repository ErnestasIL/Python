# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
# house1 = House(19900, 2025)
# house2 = House(16500, 2008)
#
# house1.country = 'LV'
#
#
#
# print(house1.country, house1.price, house1.year)
# print(house2.country, house2.price, house2.year)
#
# from datetime import datetime
#
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def get_age(self):
#         return datetime.today().year - self.year
#
#
# house1 = House(19_900, 1990)
# house2 = House(16_500, 2008)
#
# age = house1.get_age()
# print(age)
#
# print(house2.get_age())

#--------------magic methods----

# from datetime import datetime
#
# class House:
#     country = "LT"
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def get_age(self):
#         return datetime.today().year - self.year
#
#     def __str__(self):
#         return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}m senumo"
#
#
#
# houses = [
#     House(60_000, 1980),
#     House(36_000, 1970),
#     House(11_000, 2000)
# ]
# #
# # for house in houses:
# #     print(f"sena kaina: {house.price}")
# #     house.price = round(house.price * 1.21)
# #     print(f"nauja kaina: {house.price}")
# #     print('-' * 40)
#
# for house in houses:
#     print(house)


from datetime import datetime

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        return datetime.today().year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}m senumo"


houses_kaupiklis = []

while True:
    # queue_choise = input("Iveskite EXIT, kad iseiti, kitu atveju spauskite Enter:")
    # if queue_choise == 'EXIT':
    #     break
    year = int(input('Iveskite metus:'))
    price = int(input('Iveskite kaina:'))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)
    print('Spausdinam ka sukaupem:')
    for house in houses_kaupiklis:
        print(house)
















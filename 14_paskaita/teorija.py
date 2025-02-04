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
from datetime import datetime

class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        return datetime.today().year - self.year


house1 = House(19_900, 1990)
house2 = House(16_500, 2008)

age = house1.get_age()
print(age)

print(house2.get_age())








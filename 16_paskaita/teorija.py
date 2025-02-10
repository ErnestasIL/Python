
# class Gyvunas:
#     def __init__(self, vardas, spalva):
#         self.vardas = vardas
#         self.spalva = spalva
#
#     def begti(self):
#         print(f'{self.vardas} begu!!!')
#
# class Kate(Gyvunas):
#     # def __init__(self, vardas, spalva):
#     #     self.vardas = vardas
#     #     self.spalva = spalva
#     def miaukseti(self):
#         print(f'{self.vardas} sako MIAU!' )
#
# class Suo(Gyvunas):
#     def loti(self):
#         print(f'{self.vardas} loja')
#
# cat = Kate('Murkis', 'Juodas')
# cat.begti()
# cat.miaukseti()
# dog = Suo('Bobikas', 'Rudas')
# dog.loti()
#
# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, elem):
#         self.data.append(elem)
#
#     def pop(self):
#         return  self.data.pop()
#
#
# class Element:
#     def __init__(self, item1, item2):
#         self.item1 = item1
#         self.item2 = item2
#
#     def __str__(self):
#         return  f'pirmas: {self.item1}, Antras: {self.item2}'
#
# elems = [
#     Element(1, 2),
#     Element(3, 4),
#     Element(5,  6)
# ]
#
# stack = Stack()
#
# for i in elems:
#     stack.push(i)
#
# a = stack.pop()
#
# for i in stack.data:
#     print(i)
# print('-' * 20)
# print(a)



import datetime
import pickle


class House:
    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f'Namas: {self.year}, kaina: {self.price}, amzius - {self.get_age()}'


try:
    with open('namai.pickle', mode='rb') as f:
        houses_kaupiklis = pickle.load(f)
except:
    houses_kaupiklis = []

while True:

    print('1. Show all houses')
    print('2. add house')
    print('3. Remove last house')
    print('4. Exit')
    print('\n')
    try:
        user_input = int(input('Please choose action: '))
        if user_input not in range(1, 5):
            raise ValueError
    except ValueError:
        print('Please choose between 1 to 4')
        continue

    if user_input == 4:
        with open('namai.pickle', mode='wb') as f:
            pickle.dump(houses_kaupiklis, f)
        break
    elif user_input == 1:
        print()
        for house in houses_kaupiklis:
            print(house)
        print()

    elif user_input == 2:
        try:
            price = int(input('Price: '))
            year = int(input('Year: '))
            new_house = House(price, year)
            houses_kaupiklis.append(new_house)
        except ValueError:
            print('Values should be numbers')
    elif user_input == 3:
        houses_kaupiklis.pop()








# houses_kaupiklis.append(new_house)
#
# with open('namai.pickle', mode='wb') as f:
#     pickle.dump(houses_kaupiklis, f)
#
#
# for house in houses_kaupiklis:
#     print(house)











# with open('info.txt', mode='r') as file:
#     a = file.read()
# print(a)













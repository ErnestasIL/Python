
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













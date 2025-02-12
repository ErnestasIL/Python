# def apversti_teksta(tekstas):
#     return tekstas[::-1]
#
# print(apversti_teksta('labas'))
#
# def apversti_sakini(tekstas):
#     return ' '.join(tekstas.split()[::-1])
#
# print(apversti_sakini('Hello World my name is pyhton'))
#
# def sudetinga_funkcija(func):
#     for i in range(1, 10):
#         print(func('Super tekstas 123'))
#
# def super_sudetinga_funkcija(func):
#     for i in range(1, 20):
#         print(func('Labas'))
#
# # sudetinga_funkcija(apversti_sakini)
# # super_sudetinga_funkcija(apversti_teksta)
#
# def i_didiziasias(tekstas, funkcija=None):
#     if funkcija:
#         tekstas = funkcija(tekstas)
#     return tekstas.upper()
#
# print(i_didiziasias('labas', apversti_teksta))


# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self.__atlyginimas = None
#
#     def change_empoyee_name(self, vardas):
#         if not vardas:
#             raise ValueError('Name is not provided')
#         self.vardas = vardas
#
#     @staticmethod
#     def devide(a, b):
#         if b == 0:
#             raise ZeroDivisionError('Can not divide by zero')
#         return a / b
#
#     @classmethod
#     def Super_costructor(cls, vardas, pavarde, pareigos):
#         return cls(vardas, pavarde, pareigos)
#
#     @property
#     def atlyginimas(self):
#         return self.__atlyginimas

#
# def registratorius(funkcija):
#     def apvalkalas(argumentas):
#         rezultatas = funkcija(argumentas)
#         if rezultatas % 2 == 0:
#             print(f'{rezultatas} yra Lyginis')
#         else:
#             print(f'{rezultatas} yra nelyginis')
#         return rezultatas
#     return apvalkalas
#
# @registratorius
# def kvardaru(skaicius):
#     return skaicius ** 2
#
# print(kvardaru(8))

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#
#     def __iter__(self):
#         return iter([self.vardas, self.pavarde, self.pareigos, 'Labas', 'Mano', 'Vardas', self.vardas ])
#
# darbuotojas = Darbuotojas("Jonas", "Jonaitis", "Programuotojas")
# for savybe in darbuotojas:
#     print(savybe)

# listas = ['sausis', 'vasaris', 'kovas']
# listo_operatorius = iter(listas)
# print(listas)
# print(listo_operatorius)
#
# res = next(listo_operatorius)
# print(res)
# res = next(listo_operatorius)
# print(res)

# def skaiciuok_iki(max_reiksme):
#     skaicius = 0
#     while skaicius < max_reiksme:
#         yield skaicius
#         skaicius += 1
#
# for numeris in skaiciuok_iki(5):
#     print(numeris)
#

# func to count number of given word
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i

# initializing string
test_string = " There are many geeks around you, \
              geeks are known for teaching other geeks"

# count numbers of geeks used in string
count = 0
print("The number of geeks in string is : ", end="")
test_string = test_string.split()

for j in print_even(test_string):
    count = count + 1

print(count)











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


def registratorius(funkcija):
    def apvalkalas(argumentas):
        rezultatas = funkcija(argumentas)
        if rezultatas % 2 == 0:
            print(f'{rezultatas} yra Lyginis')
        else:
            print(f'{rezultatas} yra nelyginis')
        return rezultatas
    return apvalkalas

@registratorius
def kvardaru(skaicius):
    return skaicius ** 2

print(kvardaru(8))




















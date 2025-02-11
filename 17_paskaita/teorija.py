# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos, ):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self._atlyginimas = None
#         self.__asmens_kodas = None #Privatus niekur neislendantis atributas
#
#     def get_atlyginims(self):
#         if self._atlyginimas:
#             print(self._atlyginimas)
#         else:
#             print("Atlyginimas dar nepaskirtas")
#
#     def set_atlyginimas(self, suma):
#         if int(suma) > 0:
#             self._atlyginimas = suma
#         else:
#             print('Atlyginimas negali buti = 0')
#
#     def get_asmens_kodas(self):
#         if self.__asmens_kodas:
#             print(self.__asmens_kodas)
#         else:
#             print('Asmens kodas dar nepaskirtas')
#
#     def set_asmens_kodas(self, asmens_kodas):
#         if int(asmens_kodas) > 0:
#             print(self.__asmens_kodas)
#         else:
#             print('Asmens kodas negali buti = 0')
#
#
#
#     def get_darbuotojas_info(self):
#         print(f'Vardas: {self.vardas},')
#         print(f'Pavarde: {self.pavarde},')
#         print(f'Pareigos: {self.pareigos},')
#         self.__asmens_kodas()
#         self._atlyginimas()
#
# class Vadovas(Darbuotojas):
#     def __init__(self, vardas, pavarde, pareigos, departamentas):
#         super().__init__(vardas, pavarde, pareigos)
#         self.departamentas = departamentas
#
# darbuotojas1 = Darbuotojas('Jonas', 'Jonaitis', 'Programuotojas')
# darbuotojas1.set_atlyginimas('1000')
# darbuotojas1.set_asmens_kodas('318131841')
# darbuotojas1.get_darbuotojas_info()
# # vadovas1 =
# # darbuotojas1.__asmens_kodas = '123'

#-----------------------

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self.__atlyginimas = None
#     @property
#     def atlyginimas(self):
#         return self.__atlyginimas if self.__atlyginimas else 0
#
#     @atlyginimas.setter
#     def atlyginimas(self, suma):
#         self.__atlyginimas = suma if suma >= 0 else 1
#
#
#
# darb1 = Darbuotojas('Bronius', 'Laucius', 'Pagalbinis')
#
# atl = darb1.atlyginimas
# print(atl)
#
# darb1.atlyginimas = 500
# atl2 = darb1.atlyginimas
# print(atl2)

#-------------------------------------
# class Calculator:
#
#     @staticmethod
#     def add(num1, num2):
#         return num1 + num2
#
#     @staticmethod
#     def sub(num1, num2):
#         return num1 - num2
#
# a = Calculator.add(1, 2)
# print(a)
#
# b = Calculator.sub(10, 5)
# print(b)


class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    @classmethod
    def sukurk_is_vienos_eilutes(cls, eilute):
        vardas, pavarde, pareigos = eilute.split()
        return cls(vardas, pavarde, pareigos)

    def __str__(self):
        return f'Vardas: {self.vardas}. Pavarde: {self.pavarde}. Pareigos: {self.pareigos}.'

    def pakeisti_pareigas(self, naujos):
        self.pareigos = naujos

eilute = 'Jonas Jonaitis Kiemsargis'
darb = Darbuotojas.sukurk_is_vienos_eilutes(eilute)
print(darb)
darb.pakeisti_pareigas('Director')
print(darb)



























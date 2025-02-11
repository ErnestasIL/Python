class Matematika:
    @staticmethod
    def sudeti(a, b):
        return a + b
    @staticmethod
    def atimti(a, b):
        return a - b
    @staticmethod
    def dauginti(a, b):
        return a * b
    @staticmethod
    def dalinti(a, b):
        return a / b
    @staticmethod
    def ar_lyginis(a):
        if a % 2 == 0:
            return 'Lyginis'
        else:
            return 'Nelyginis'

print(Matematika.sudeti(10, 5))
print(Matematika.atimti(10, 5))
print(Matematika.dauginti(10, 5))
print(Matematika.dalinti(10, 5))
print(Matematika.ar_lyginis(10))
print('-' * 30)

class Automobilis:
    def __init__(self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    @classmethod
    def sukurti_is_string(cls, eilute):
        marke, modelis, metai = eilute.split()
        return cls(marke, modelis, metai)

    @classmethod
    def naujausias_modelis(cls, auto_sarasas):
        auto_objektai = [cls.sukurti_is_string(eilute) for eilute in auto_sarasas]
        naujausias = max(auto_objektai, key=lambda auto: auto.metai)
        return naujausias

    def __str__(self):
        return f'Automobilio marke: {self.marke}, modelis: {self.modelis}, metai: {self.metai}'

autos = [
'Toyota Corolla 2019',
'Toyota Auris 2015',
'Toyota Yaris 2023',
'Toyota Prius 2010'
]

automobilis = 'Toyota Corolla 2019'

auto = Automobilis.sukurti_is_string(automobilis)
print(auto)

print('-' * 30)

naujausias = Automobilis.naujausias_modelis(autos)
print(naujausias)
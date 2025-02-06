class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos
    def __str__(self):
        return f'Darbuotojo Vardas: {self.vardas}, jam: {self.amzius}m. ir jis yra: {self.pareigos}'

darbininkas = Darbuotojas('Kestas', '40', 'kiemsargis')

print(darbininkas)
print('-' * 30)
#---------

class TransportoPriemone:
    def judeti(self):
        print(f'Transporto priemone juda')

class Dviratis(TransportoPriemone):
    def judeti(self):
        print(f'Dviratis vaziuoja pedalais')


traktor = TransportoPriemone()
dviratis = Dviratis()


traktor.judeti()
print('-' * 30)
dviratis.judeti()








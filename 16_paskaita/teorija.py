
class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f'{self.vardas} begu!!!')

class Kate(Gyvunas):
    # def __init__(self, vardas, spalva):
    #     self.vardas = vardas
    #     self.spalva = spalva
    def miaukseti(self):
        print(f'{self.vardas} sako MIAU!' )

class Suo(Gyvunas):
    def loti(self):
        print(f'{self.vardas} loja')

cat = Kate('Murkis', 'Juodas')
cat.begti()
cat.miaukseti()
dog = Suo('Bobikas', 'Rudas')
dog.loti()





















class Darbuotojas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = 0

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, suma):
        if suma >= 500:
            self.__atlyginimas = suma
        else:
            raise ValueError('Negali gauti maziau negu 500 pinigu')

    @property
    def mokesciai(self):
        return self.__atlyginimas * 0.2



darb = Darbuotojas('Kazys', 'Petrovas')
darb.atlyginimas = 1200
atl = darb.atlyginimas
mokes = darb.mokesciai

print(f'Atlyginimas: {atl}')
print(f'Mokesciai: {mokes}')
print('-' * 20)
try:darb.atlyginimas = 400
except ValueError as e:
    print(f'Klaida: {e}')

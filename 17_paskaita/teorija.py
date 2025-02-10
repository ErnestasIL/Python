class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos, ):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self._atlyginimas = None
        self.__asmens_kodas = None #Privatus niekur neislendantis atributas

    def get_atlyginims(self):
        if self._atlyginimas:
            print(self._atlyginimas)
        else:
            print("Atlyginimas dar nepaskirtas")

    def set_atlyginimas(self, suma):
        if int(suma) > 0:
            self._atlyginimas = suma
        else:
            print('Atlyginimas negali buti = 0')

    def get_asmens_kodas(self):
        if self.__asmens_kodas:
            print(self.__asmens_kodas)
        else:
            print('Asmens kodas dar nepaskirtas')

    def set_asmens_kodas(self, asmens_kodas):
        if int(asmens_kodas) > 0:
            print(self.__asmens_kodas)
        else:
            print('Asmens kodas negali buti = 0')



    def get_darbuotojas_info(self):
        print(f'Vardas: {self.vardas},')
        print(f'Pavarde: {self.pavarde},')
        print(f'Pareigos: {self.pareigos},')
        self.__asmens_kodas()
        self._atlyginimas()

class Vadovas(Darbuotojas):
    def __init__(self, vardas, pavarde, pareigos, departamentas):
        super().__init__(vardas, pavarde, pareigos)
        self.departamentas = departamentas

darbuotojas1 = Darbuotojas('Jonas', 'Jonaitis', 'Programuotojas')
darbuotojas1.set_atlyginimas('1000')
darbuotojas1.set_asmens_kodas('318131841')
darbuotojas1.get_darbuotojas_info()
# vadovas1 =
# darbuotojas1.__asmens_kodas = '123'
class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazimys):
        if 1 <= pazimys <= 10:
            self._pazymiai.append(pazimys)
            print(f'Pazymys: {self._pazymiai} ')
        else:
            print('Neteisingas pazimys')

    def rodyti_vidurki(self):
        if self._pazymiai:
            vidurkis = sum(self._pazymiai) / len(self._pazymiai)
            print(f'Pazymiu vidurkis: {round(vidurkis)}')
        else:
            print('Error')



class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonus):
        self.bonus = bonus
        super().__init__(vardas, pavarde)

    def add_bonus(self):
        if self._pazymiai:
            vidurkis = (sum(self._pazymiai) + self.bonus) / len(self._pazymiai)
            print(f'vidurkis su bonusu: {round(vidurkis)}')
        else:
            print('Error')


studentas = Studentas('Bronius', 'Pop')


studentas.prideti_pazymi(2)
studentas.prideti_pazymi(2)
studentas.prideti_pazymi(2)
studentas.rodyti_vidurki()
print('-' * 20)
lyderis = StudentasLyderis('Kazys', 'Bo', bonus=5)
lyderis.prideti_pazymi(2)
lyderis.prideti_pazymi(2)
lyderis.prideti_pazymi(2)
lyderis.add_bonus()

print('-' * 20)

class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.__balansas = 0

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
            print(f"Prideta {suma}$. balansas: {self.__balansas}$")
        else:
            print("Suma negali buti neigiama.")

    def nuskaiciuoti_pinigus(self, suma):
        if suma > 0:
            if self.__balansas >= suma:
                self.__balansas -= suma
                print(f"Nuskaiciuota {suma}$. likutis: {self.__balansas}$")
            else:
                print("Nepakanka lesu operacijai atlikti.")
        else:
            print("Suma turi buti teigiama.")


saskaita = BankoSaskaita("Pete")
saskaita.prideti_pinigus(200)
saskaita.nuskaiciuoti_pinigus(50)
print(f"balanso likutis: {saskaita.gauti_balansa()}$")
saskaita.nuskaiciuoti_pinigus(100)


# print(saskaita.__balansas)


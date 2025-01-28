#--------- moduliai-----------

import random

atsitiktinis_skaicius = random.randint(1, 10)

print(f'Atsitiktinis int skaicius nuo 1 iki 10: {atsitiktinis_skaicius}')
print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1, 10)}')

while True:
    skaicius = int(input('Iveskite skaiciu, kol neatpesite tinkamo neiseisite:'))
    if skaicius == random.randint(1, 10):
        break
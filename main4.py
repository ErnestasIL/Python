#ciklai
from itertools import count

# menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']
#
# for elementas in menesiai:
#     print(elementas)
#     print(elementas.upper())
#     print('***')
#     a = 1
#     b = 2
#     c = a + b
#
# print('---------')
#
# skaiciai = [10 , 7, 50, 111]
# for elem in skaiciai:
#     print(elem * 100)
#
# print('---------')
#
#
# suma = 0
# for elem in skaiciai:
#     suma += elem
#
# print(suma)


# print('---------')


# suma = 0
# for elem in skaiciai:
#     suma += elem * 100
#     print(suma)
# print(suma)

# suma = 0
# for elem in skaiciai[:: 2]:
#     suma += elem
# print(suma)


# task!!!

# menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']
#
# for elem in menesiai:
#     print(f' menuo {elem}')
#
#
# skaiciai = [5, 10, 15, 20]
#
# suma = 0
# for elem in skaiciai:
#     suma += elem
#
# print(suma)
#
# for elem in skaiciai:
#     # print(elem * 2)

#
# skaiciai = [10, 5, 50, 111]
# tuscias = []
#
# #len - listo, ilgis elementu skaicius
#
# print(len(skaiciai))
# print(len(tuscias))
#
# string = 'ABC'
# print(len(string))
#
# #sum - skaiciuoja elementu suma
#
# print(sum(skaiciai))
# # print(sum(string))  negalima
#
#
# #max - suranda didziausia skaiciu
#
# print(max(skaiciai))
#
# #min - maziausias skaicius
# print(min(skaiciai))


#task!!!!

# numbers = [3, 8, 12, 5, 10]
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))


# m = ['sausis', 'vasaris,', 'kovas', 'balandis', 'geguze', 'birzelis']
# print(m)
# print(m[0])
# print(m[2])
# print(m[-1])
#
#
# #slicenimas
#
# print(m[1:4])
# print(m[1:3 + 1])
# print(m[1:])
# print(m[:5])
#
# print('--------')
# #zingsniai
#
# print(m[::3]) #kas trecias
# print(m[::-1]) #atvercia
# print(m[::-2]) # atvercia ir paima kas antra
#
#
# print('--------')
#
#
# print(type(m[4])) #gaunam string pasiemam pagal jo tipa
# print(m[4][1]) #galima paimt kiekvieno elemento atskira elementa
#
#
# print(m[4][1:5:2].upper()) # galima naudot atskira slice ir panaudot kitiem dalykam


#task

# salys = ['Lietuva', 'Latvija', 'Estija', 'Lenkija']
#
# print(salys[0])
# print(salys[-1])
# print(salys[1:-1])
# print(salys[::-1])

#tuplas negalim istrynt ar keisti

# menesiai = ('sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis')
# print(type(menesiai))
# for elem in menesiai:
#     print(elem)
# print(menesiai[1])
# print(menesiai[2])
# print(menesiai[-1])
# print(menesiai[1:3])
# print(menesiai[3:5])
# print(menesiai.index('kovas'))
# print(menesiai.count('sausis'))



#task

# days = ('pirmadienis', 'antradienis', 'treciadienis', 'ketvirtadienis')
#
# print(days[1])
# print(days.count('pirmadienis'))
# print(days.index('pirmadienis'))

#sarasai sarasuose

# darbuotojai = [
#     ['Valdas', 'programuotojas', 2000],
#     ['Adomas', 'direktorius', 3000],
#     ['Aldona', 'vadybininkas', 1800],
#     ['Jogaila', 'programuotojas', 2500]
# ]

#
# print(darbuotojai)
# print(darbuotojai[0])
# print(darbuotojai[0][1])
# print(darbuotojai[0][1].upper())
#
# # for darbuotojas in darbuotojai:
# #     print(darbuotojas)
#
# for darbuotojas in darbuotojai:
#     print(darbuotojas[0], darbuotojas[2])
#
# for vardas, pareigos, atlyginimas in darbuotojai:
#     print(atlyginimas, vardas, pareigos)


# suma = 0
# for vardas, pareigos, atlygnimas in darbuotojai:
#     suma += atlygnimas
# print(suma)
#
# atlygnimai = []
# for vardas, pareigos, atlygnimas in darbuotojai:
#     atlygnimai.append(atlygnimas)
# print(atlygnimai)
# print(sum(atlygnimai))

# pozicijos = []
# for vardas, pareigos, atlyginimas in darbuotojai:
#     pozicijos.append(pareigos)
# print(pozicijos)
# print(pozicijos.count('programuotojas'))



#string metodai sarasams

# #.split metodas
# months_str = "sausis vasaris kovas"
# print(months_str)
#
# months_list = months_str.split(' ')#gali atskirt nebuinai pagal tarpa
# print(months_list)
#
# #.join metodas
#
# joined_string = ' '.join(months_list)
# print(joined_string)
#
#
# x_list = ['Adomas']
# print('-'.join(x_list))

#task!!

fruit = 'obuolys bananai kriauses'
fruit_list = fruit.split(' ')
print(fruit_list)
print('---'.join(fruit_list))
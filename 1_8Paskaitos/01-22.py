# marke = 'Audi'
# model = 'A6'
# auto = {}
# print(auto)
#
# if marke == 'Audi':
#     auto['marke'] = marke
# auto['model'] = model
# print(auto)
#
# auto['marke'] = 'BMW'
# auto['model'] = '5'
#
# auto['colors'] = ['red', 'white', 'black']
#
# car_tech_charateristics = {
#     'engine': 3.0,
#     'interior': 'leather'
# }
#
# auto.update(car_tech_charateristics)
# auto.update({
#     'year': 2026,
#     'eco2000': True
# })
# print(auto)
import pprint

# marke = 'Audi'
# model = 'A6'
# auto = {}
# print(auto)
#
# if marke == 'Audi':
#     auto['marke'] = marke
# auto['model'] = model
# print(auto)
#
# auto['marke'] = 'BMW'
# auto['model'] = '5'
#
# auto['colors'] = ['red', 'white', 'black']
#
# car_tech_charateristics = {
#     'engine': 3.0,
#     'interior': 'leather'
# }
#
# auto.update(car_tech_charateristics)
# auto.update({
#     'year': 2026,
#     'eco2000': True
# })
#
# del auto['eco2000']
# interior = auto.pop('interior')
# auto['gas_engine'] = auto.pop('engine')
# auto['year'] = 2000
# auto['year'] += 5
# auto['colors'].append('yellow')
# print(auto)
# print(interior)

                                            #!!Task!!!

# store = {
#     "name": "E-Shop",
#     "categories": ["Electronics", "Books", "Clothing"],
#     "products": [
#         {"name": "Laptop", "price": 1000, "stock": 10},
#         {"name": "Book", "price": 20, "stock": 50},
#         {"name": "T-shirt", "price": 15, "stock": 100}
#     ],
#     "rating": 4.5
# }
# stock_increase = 0
# store['categories'].remove('Clothing')
# pprint.pprint(store['categories'])
# for product in store['products']:
#     if product['price'] > 50:
#         product['price'] *= 0.95
#     if product['name'] == 'Laptop':
#         product['stock'] = 15
# pprint.pprint(store['products'])
#
#
#
#
# if store['rating'] < 4.6:
#     store['rating'] += 0.1
# print(f'store rating now is: {store["rating"]}')


# a = True
# while a:
#     print('123')
#     break
#
# objektas = [1, 2, 3, 4, 5]
# for element in objektas:
#     if element == 2:
#         continue
#     print(element)
#

# skaitiklis = 0
# while skaitiklis <= 5:
#     print(f'skaitiklis yra : {skaitiklis}')
#     print('---------')
#     skaitiklis += 1
#
# while True:
#     user_input = input('Provide number: ')
#     if user_input == 'stop':
#         break
#     print('your number ')

# while True:
#     print('kartojimo pradzia')
#     print('1. sis menu punktas nedaro nieko\n'
#           '2. iseiti is kartojimo bloko\n'
#           '3. vel parodyti meniu')
#     pasirinkimas = input('pasirinkimas: ')
#     if pasirinkimas == '2':
#         break
#     elif pasirinkimas == '3':
#         continue
#     else:
#         print('nebuvo nieko pasirinkta')
#     print('kartojimo pabaiga')

                                                #task!!
# total_sum = 0
# while True:
#     user_input = int(input('Iveskite skaiciu nuo 1 iki 10:'))
#     if user_input < 1 or user_input > 10:
#         print('Skaicius turi buti nuo 1 iki 10')
#         continue
#     if user_input == 5:
#         print('Ciklas nutrauktas')
#         break
#     total_sum += user_input
# print(f'Skaiciu suma: {total_sum}')

#-------------------------------------

# while True:
#     print("1. atlikti skaičiaus daugybą\n"
#           "2. išeiti")
#
#     pasirinkimas = input()
#     if pasirinkimas == "2":
#         break
#     if pasirinkimas == "1":
#         # daugyba tęsis, kol nebus paspausta q
#         while True:
#             print("Įvesti skaičių daugybai iš 100 arba q - grįžti")
#             ivestis = input()
#             if ivestis == "q":
#                 break
#             elif not ivestis.isdigit():
#                 print("Įvestas ne skaičius!!!")
#                 continue
#             skaicius = int(ivestis) * 100
#             print("Daugybos iš 100 rezultatas -", skaicius)


# for skaicius in range(1, 6):
#     print(f'dabartinis skaicius {skaicius}')


# listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# flag5 = False
# flag3 = False
# for elem in listas:
#     print(elem)
#     if elem % 5 == 0:
#         flag5 = True
#     if elem % 3 == 0:
#         flag3 = True
#     if flag5 and flag5:
#         break
# if flag5:
#     print('Dalinasi is 5')
# if flag3:
#     print('Dalinasi is 3')

# listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # suma
# suma = 0
# for elem in listas:
#     suma += elem  # kaupiame sumą
# print("Suma yra:", suma)
#
# # maksimalus skaičius
# maksimalus = listas[0]
# for elem in listas:
#     if elem > maksimalus:
#         maksimalus = elem  # randame maksimalų elementą
# print("Maksimalus yra:", maksimalus)


                        #Task!!!


numbers = [5, 7, 15, 6, 3, 20, 12]

for elem in numbers:
    if elem % 2 == 0 or elem % 5 == 0:
        print(elem)
    if elem > 10:
        break


negative_numbers = [-10, -5, 0, 5, 10, 15, 20]
neg_sum = 0
pos_sum= 0
max_numb = negative_numbers[0]
min_numb = negative_numbers[0]
for numb in negative_numbers:
    if numb > 0:
        pos_sum += numb
    if numb < 0:
        neg_sum += numb
    if numb > max_numb:
        max_numb = numb
    if numb < min_numb:
        min_numb = numb
print(pos_sum)
print(neg_sum)
print(f'max number {max_numb}')
print(f'min number {min_numb}')

#salygos
# numb1 = 100
# numb2 = 500
# numb3 = 100
#
# # a = numb1 == numb2
# # print(type(a) is bool) # yes true
# # print(type(numb1) is bool) #no false
# # print(type(numb1) is int) # yes true
#
# char = 'A'
# text = 'ABCD'
# text2 = 'QWER'
#
# print(char in text)
#
# print(char in text2)
# print('O' in 'PROJECT')
#
# name = 'John'
# names_list = ['Donald', 'Ona', 'Petras']
# print(name in names_list)
#
# # print(numb1 < numb2)
# # print(numb1 > numb2)
# # print(numb1 == numb3)
# # print(numb1 != numb3)


#task!!

# num1 = float(input('number 1:'))
# num2 = float(input('number 2:'))
# if num1 > num2:
#     print(int(num1))
# else:print(int(num2))

# numb = int(input('number:'))
# print(numb % 2 == 0)
# if numb % 2:
#     print('Even')
# else:print('Odd')


# names = ['petras', 'bronius', 'stasys', 'maryte']
# name = input('your name:')
# print(name in names)

#if

# numb1 = 100
# numb2 = 500
# if numb1 > numb2:
#     print(f'{numb1} yra didesnis uz {numb2}')
# else:print(f'{numb1} yra mazesnis uz {numb2}')
#
# a = 100
# b = 500
# c = 300
# if a > b > c:
#     print('labas')
# else:print('ate')

#task!!!!


# age = int(input('Your age:'))
# if age <= 18:
#     print('under age')
# else:print('above age')
#
# temp = int(input('temperature:'))
# if temp <= 0:
#     print('cold')
# if 0 <= temp <= 20:
#     print("mid")
# if temp > 20:
#     print("hot")


#
# numb1 = 100
# numb2 = 500
#
# if numb1 > numb2:
#     print('hello')
# elif numb1 == numb2:
#     print('same')
# else:print('shit')


# task!!!
# score = int(input('your score:'))
# if 0 <= score <= 4:
#     print('too low')
# elif 5 <= score <= 7:
#     print('mid')
# elif 8 <= score == 10:
#     print('great')
# else:print('error, please write up to 10')



# season = input('write a season:')
# if season == 'ziema':
#     print('gruodis, sausis, vasaris')
# elif season == 'pavasaris':
#     print('kovas, balaandis, geguze')
# elif season == 'vasara':
#     print('birzelis, liepa, rugpjutis')
# elif season == 'ruduo':
#     print('rugsejis, spalis, lapkritis')
# else:print('not a season')

# auto = "Audi"
# autos_ger = ["BMW", "Audi", "Mercedes"]
# autos_it = ["Ferrari", "Lamborghini"]
# autos_sport = ["BMW", "Ferrari"]
#
# if ((auto in autos_ger) or (auto in autos_it)) and (auto in autos_sport):
#     print(auto, "yra vokiškas-sportinis arba itališkas-sportinis")
# else:
#     print(auto, "nėra tarp sportinių itališkų arba vokiškų")

#task!!!

# num1 = int(input('Nr 1:'))
# num2 = int(input('Nr 1:'))
# # if num1 > 0 and num2 > 0:
# #     print('plius')
#
# if num1 < 0 or num2 < 0:
#     print('minus')

# brand = input('Your car brand:')
# model = input('Your car model:')
# car = ['BMW', 'Audi', 'toyota', 'Wolksvagen']
# sport = ['M3', 'supra', 'ss']
#
# if brand in car and model in sport:
#     print('wroom')

#sutrumpintas if

# numb4 = 9
# if numb4 % 2 == 0:
#     result = 'lygus'
# else: result = 'nelygus'
# print(result)
# print('-----------')
# numb4 = 8
# result = 'lygus' if numb4 % 2 == 0 else 'nelygus'
# print(result)


#task!!!

print('teigiamas' if float(input("Ivskite skaiciu:")) > 0 else 'neigiamas')

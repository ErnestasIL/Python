# 2 uzduotis DUOMENU TIPAI

# numb1 = 10  # int
# numb2 = 1.5  #float
# text = "Hello"  #string
#
#
#
# print(numb1)
# print(numb2)
# print(text)
#
# print(type(numb1))
# print(type(numb2))
# print(type(text))
#
# res = numb1 + numb2
# print(res)
# print(type(res))

# user_input = input('iveskite teksta: ')
#
# print(type(user_input))



weight = int(input('iveskite svory: '))
height = float(input("iveskite ugi: "))
res = weight / ((height /100) ** 2)
# print('Jusu BMI:', int(res))
print(f'jusu BMI yra: {round(res , 1)}')
# print(f"Your BMI: {float(input('Mass kg: ')) / ((float(input('height cm: ')) / 100) ** 2)}")

#simboliu indeksavimas

text1 = 'ABCDE' #skaiciuoja nuo 0

print(text1[3])    #skaiciuoja nuo 0

print(text1[-1]) #pirmas skaicius nuo galo etc.

#slicing

text2 = 'ABCDE'
print(text1[0:2])  #paima pirmas 2 raides
print(text1[1:4])  #paimi is vidurio random variantas
print(text1[1:-1])  #galima paimi skaiciuojant is galo
print(text1[1:])  #paima viska nuo antro
print(text1[:4])  #galima atvirksciai


#uzduotis

text3 = 'Hello World'
print(text3[0:5])
print(text3[:5])
print(text3[6:])
print(text3[:7])
print(text3[1:7])
print(text3[1:-1])
print(text3[5])
print("'" + text3[5] + "'")
print('Task done!')

#stringu metodai

text = 'hello world!'
text5 = text.upper() #konvertuoja i didziasas

print(text)
print(text5)
print(text.count('l')) #skaiciuja kiek kazko yra
print(text.count('ll'))

print(text.index('r')) # randa keilntas yra indekse sarase iesko pirmo jei neranda error
print(text.find('find')) #gauna -1 index meta error seip tas pats kas index

text = text.replace('l', 'w') # keicia teksta galima pakeist ir zodzius
print(text)
user = ' Erne ftw         '
print(user.strip())  #pasalina tarpus nuo priekio ir galo


month = 'sausis'
day = 14
ftext = f'Menesis yra {month}, diena yra {day} d'
print(ftext)

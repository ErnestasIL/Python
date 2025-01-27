#true false metodai

# city1 = 'Vilnius'
# city2 = 'Kaunas'
#
# print(city1.istitle())  #ar is didziosios
#
# print(city2.isupper()) # ar visos didziosios
#
# print(city1.startswith('Viln'))  # tikrina ar prasideda is kazkokios raides ar raidziu pradzios
#
word = str(input('write a word:'))

# if word.istitle():
#     print('Starts with uppercase')
# else: print('Starts with lowercase')

# if word.istitle() :
#     print('Yay')
# elif word.islower():
#     print('Hay')
# else:print('Nay')

if word.startswith('A'):
    print('Aha')
elif word.isupper():
    print('Oho')
else:print('Nono')

# Task 1-2
eilute = input('Įveskite sakinį/simbolį: ')
ar_prasideda_didz = 'Didžioji raidė' if eilute.istitle() else 'Mažoji raidė'
print(ar_prasideda_didz)

print('Didžioji raidė' if input('Įveskite sakinį/simbolį: ').istitle() else 'Mažoji raidė')

# Task 1
zodis = input('Įveskite žodį: ') # vilnius
ar_prasideda_didz = zodis.istitle()

ar_mazosios = zodis.islower() # True
ar_mazosios = not zodis.isupper() # True

print(f'Žodis prasideda didžiąja raide: {ar_prasideda_didz}')
print(f'Visi žodžio simboliai yra mažosios raidės: {ar_mazosios}')

# Task 2
eilute = input('Įveskite sakinį: ')
ar_prasideda_A = eilute.startswith('A')
ar_didziosios = eilute.isupper()
print(f'Eilutė prasideda simboliu „A“: {ar_prasideda_A}')
print(f'Eilutė parašyta tik didžiosiomis raidėmis: {ar_didziosios}')




# 3 lines
number = float(input('Įveskite skaičių: '))
result = 'Teigiamas' if number > 0 else 'Neigiamas'
print(result)

# 1 line
print('Teigiamas' if (number := float(input('Įveskite skaičių: '))) > 0 else 'Neigiamas' if number != 0 else 'Nulis')

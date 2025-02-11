def sekimo_dekoratorius(func):
    def apvalkalas(a, b):
        print(f'Vykdoma funkcija: {func.__name__}')
        res = func(a, b)
        print('Funkcija baigta!')
        return res
    return apvalkalas

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b

@sekimo_dekoratorius
def dalinti(a, b):
    if b == 0:
        return 'dalyba is nulio negalima'
    return a / b


print(dauginti(4, 5))
print('-' * 20)
print(dalinti(10, 2))
print('-' * 20)
print(dalinti(10, 0))

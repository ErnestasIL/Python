#-------1------
def add_numbers(*args):
    return sum(args)

print(add_numbers(5, 10, 15))
print(add_numbers(100, 200, 300, 400))
#-------2-------

def sveikinti_vardus(*args):
    res = ''
    for name in args:
        res += f'Laba diena, {name}!\n'
    return res

print(sveikinti_vardus('Jonas', 'Asta', 'Mantas'))

#-------3--------

def pakelti_laipsniu(numb, *args):
    for elem in args:
        print(elem ** numb)

print(pakelti_laipsniu(3, 10, 5, 15, 8))
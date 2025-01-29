def spausdinti_zinutes(kartai, *args, pabaiga="!"):
    for elem in args:
        print(f'{kartai * elem}{pabaiga}')

spausdinti_zinutes(3, 'labas ','krabas ', pabaiga='yaaaa')

#------------------

def dauginti_skaicius(n, *args):
    return [i * n for i in args]

print(dauginti_skaicius(6, 12, 15, 2, 10))
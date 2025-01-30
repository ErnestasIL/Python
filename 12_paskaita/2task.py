while True:
    number1 = input('Iveskite skaiciu: ')
    number2 = input('Iveskite skaiciu is kurio norite padalinti: ')

    try:
        skaicius = int(number1)
        daliklis = int(number2)
        res = skaicius / daliklis
        print(f'Rezultatas: {res}')
    except ZeroDivisionError as zero:
        print(f'Ivedete nuli ir gavote error: {zero}')
    except ValueError as val:
        print(f'Ivedete ne skaiciu ir gavote error: {val}')

    print('-------------------')

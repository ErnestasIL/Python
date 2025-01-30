#-----------Try/accept-----------

# ivestis = '4'
#
# try:
#     skaicius = int(ivestis)
#     res = skaicius / 0
# except Exception as ex:
#     print('Mes crashinom, taciau suvaldem crash')
#     print(ex)
#     print(ex.__class__)
#
# print('Hello, Im still working')

#---------konkretus except klaidu gaudymas--------

while True:
    ivestis1 = input('iveskite skaiciu: ')
    ivestis2 = input('iveskite dalikli: ')

    try:
        skaicius = int(ivestis1)
        daliklis = int(ivestis2)
        res = skaicius / daliklis
        print(f'Rezultatas: {res}')
    except ZeroDivisionError:
        print('Pakeiskite dalikli is 0 i kita')
    except ValueError:
        print('Paleiskite programa is naujo ir irasykite skaiciu')
    print('-------------------------')











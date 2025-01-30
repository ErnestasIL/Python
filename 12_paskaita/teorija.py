#-----------Try/accept-----------

ivestis = '4'

try:
    skaicius = int(ivestis)
    res = skaicius / 0
except Exception as ex:
    print('Mes crashinom, taciau suvaldem crash')
    print(ex)
    print(ex.__class__)

print('Hello, Im still working')















def prideti_zenkliuka(tekstas):
    return tekstas + '*'

print(prideti_zenkliuka('tekstas'))

def apversti_teksta(tekstas):
    return tekstas[::-1]

print(apversti_teksta('nedapasikiskiokopusteliaudamas'))

def apdoroti_teksta(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.lower()

print(apdoroti_teksta('LaBaNaKt', apversti_teksta))


def keli_apdorojimai(tekstas, *funkcijos):
    for funkcija in funkcijos:
        tekstas = funkcija(tekstas)
    return tekstas

print(keli_apdorojimai('labas', prideti_zenkliuka, apversti_teksta))
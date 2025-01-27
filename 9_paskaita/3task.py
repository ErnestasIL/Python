def greeting(name1, name2, name3):
    if not name1 or not name2 or not name3:
        return
    hello_string = f'Labas, {name1}!, Labas {name2}!, Labas {name3} '
    return hello_string

print(greeting('Bronius', 'Stasys', 'Petras'))



print('------------------------------------------')


def sveikink_su_pavadinimu(vardas, pavadinimas = 'drauge'):
    print(f'Sveikas {vardas}! Ka veiki, {pavadinimas}')

sveikink_su_pavadinimu('Kazys')
# print(sveikink_su_pavadinimu('Kazys', 'kolega'))
sveikink_su_pavadinimu(
    vardas='Kazys',
    pavadinimas= 'kolega')



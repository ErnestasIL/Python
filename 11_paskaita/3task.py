def rodyti_duomenis(**kwargs):
    for raktas, reiksme in kwargs.items():
        print(f'{raktas}: {reiksme}')
rodyti_duomenis(vardas="Petras", pavarde="Petraitis", miestas="Prienai")

print('---------------------')

def registruoti_naudotoja(vardas, el_pastas, **kwargs):
    print(f"Vardas: {vardas}\nEl. paštas: {el_pastas}")
    for raktas, reiksme in kwargs.items():
        print(f"{raktas}: {reiksme}")

registruoti_naudotoja('John', 'john.cena@cantseeme.com', ocupation='wrestler', lytis='male')
print('---------------------')

def atspausdinti_lista(listas, **kwargs):
    print(*listas, **kwargs)


atspausdinti_lista(['something', 'creeping', 'behind', 'you'], sep=' @@ ', end=' ^.^ ')
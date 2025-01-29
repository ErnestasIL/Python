def rodyti_duomenis(**kwargs):
    print(kwargs)

rodyti_duomenis(vardas="Petras", pavarde="Petraitis", gim_metai=1991, lytis='vyras')

def registruoti_naudotoja(vardas, el_pastas, **kwargs):
    print(f"Vardas: {vardas}\nEl. paštas: {el_pastas}")
    for raktas, reiksme in kwargs.items():
        print(f"{raktas}: {reiksme}")

registruoti_naudotoja('John', 'john.cena@cantseeme.com', ocupation='wrestler', lytis='male')

random_list = ['something', 'creeping', 'behind', 'you']
def atspausdinti_lista(listas, **kwargs):
    for elem in listas:
        print(elem, 'its_me', **kwargs)


atspausdinti_lista(random_list, sep=' @@ ', end=' ^.^ ')
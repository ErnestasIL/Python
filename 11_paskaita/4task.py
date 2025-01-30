pakelti_kvadratu = lambda a: a ** 2

print(pakelti_kvadratu(9))

darbuotojai = [('Jonas', 2500), ('Asta', 3200), ('Mantas', 2100)]

res = sorted(darbuotojai, key=lambda pay:pay[1] )

print(res)


skaiciai = [5, 10, 15, 20, 25, 30]

res2 = list(filter(lambda x: x % 10 == 0, skaiciai))

print(res2)
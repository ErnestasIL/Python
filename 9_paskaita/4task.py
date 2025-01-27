#1task

def skaiciuoti_sumos_tipa(numb1, numb2, tik_teikgiama=False):
    suma = numb1 + numb2
    if tik_teikgiama:
        suma = max(suma, 0)
    return suma

print(skaiciuoti_sumos_tipa(1, -3 ))
print(skaiciuoti_sumos_tipa(1, -3, True ))
print(skaiciuoti_sumos_tipa(1, 3, True ))


#2task

def apskaiciuok_vidurki(skaiciai):
    """
    Apskaičiuoja ir grąžina sąrašo skaičių vidurkį.

    Argumentai:
    skaiciai (list): Sąrašas skaičių, kurių vidurkį reikia apskaičiuoti.

    Grąžinama reikšmė:
    float: Sąrašo skaičių vidurkis. Jei sąrašas tuščias, grąžinama 0.
    """
    if not skaiciai:
        return 0
    return sum(skaiciai) / len(skaiciai)

print(apskaiciuok_vidurki([3, 15, 12, 11, 5, 7]))
#3task

def prideti_zodi(tekstas: str, zodis: str) -> str:
    return tekstas + ' ' + zodis

res= prideti_zodi('As gale', 'Pradzia ')
print(res)
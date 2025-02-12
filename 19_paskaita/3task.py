import sqlite3

conn = sqlite3.connect('mokykla.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS mokykla (
        pavadinimas TEXT,
        adresas TEXT,
        mokiniu_skaicius INTEGER
    )
''')
conn.commit()


def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    c.execute('''
        INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius)
        VALUES (?, ?, ?)
    ''', (pavadinimas, adresas, mokiniu_skaicius))
    conn.commit()


def skaityti_mokyklas(min_mokiniu_skaicius=0):
    c.execute('SELECT * FROM mokykla WHERE mokiniu_skaicius > ?', (min_mokiniu_skaicius,))

    mokyklos = c.fetchall()

    for mokykla in mokyklos:
        print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokiniu skaicius: {mokykla[2]}")

def atnaujinti_mokiniu_skaicius(pavadinimas, mokiniu_skaicius):
    c.execute('UPDATE mokykla SET mokiniu_skaicius = ? WHERE pavadinimas = ?', (mokiniu_skaicius, pavadinimas))
    conn.commit()

skaityti_mokyklas()
print('-' * 40)
atnaujinti_mokiniu_skaicius('Kauno gimnazija', 969)

skaityti_mokyklas()
conn.close()
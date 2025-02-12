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

def skaityti_mokyklas(min_mokiniu_skaicius=None):
    if min_mokiniu_skaicius is not None:
        c.execute('SELECT * FROM mokykla WHERE mokiniu_skaicius > ?', (min_mokiniu_skaicius,))
    else:
        c.execute('SELECT * FROM mokykla')

    mokyklos = c.fetchall()
    for mokykla in mokyklos:
        print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokiniu skaicius: {mokykla[2]}")


prideti_mokykla('Vilniaus progimnazija', 'Vilniaus g. 10', 500)
prideti_mokykla('Kauno gimnazija', 'Kauno g. 5', 800)

print('Visos mokyklos:')
skaityti_mokyklas()


print('\nMokyklos su daugiau nei 600 mokiniu:')
skaityti_mokyklas(600)

conn.close()
import sqlite3

def init_database():
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        c.execute(
            '''CREATE TABLE IF NOT EXISTS studentai (
                vardas TEXT,
                pavarde TEXT,
                klase INTEGER)'''
        )
        conn.commit()

def append_to_studentai(vardas, pavarde, klase):
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)", (vardas, pavarde, klase))

def print_all_studentai_rows():
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM studentai"):
            print(row)

def print_all_studentai_names():
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT vardas FROM studentai"):
            print(row[0])


init_database()

append_to_studentai('John', 'Jonaitis', 11)
append_to_studentai('Gitanas', 'Nauseda', 11)
append_to_studentai('Dalia', 'Grybauskaite', 11)

print_all_studentai_names()

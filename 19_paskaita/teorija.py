import cmath
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

def change_klase_by_namme(klase, vardas):
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        c.execute('UPDATE studentai SET klase = ? WHERE vardas = ?', (klase, vardas))

def remove_row_by_name(vardas):
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM studentai WHERE vardas = ?', (vardas,))

def delete_all():
    with sqlite3.connect('pavizdys.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM studentai')

remove_row_by_name('John')

change_klase_by_namme(10, 'Dalia')
print_all_studentai_rows()
delete_all()

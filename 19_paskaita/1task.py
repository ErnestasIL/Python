import sqlite3

conn = sqlite3.connect('mokykla.db')

c = conn.cursor()

c.execute(
'''
    CREATE TABLE IF NOT EXISTS sudentai (
    pavadinimas TEXT,
    adresas TEXT,
    mokyniu_skaicius INTEGER)
'''
)

conn.commit()
conn.close()
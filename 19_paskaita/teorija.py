import sqlite3

conn = sqlite3.connect('pavizdys.db')

c = conn.cursor()

c.execute(
'''
    CREATE TABLE IF NOT EXISTS sudentai (
    vardas TEXT,
    pavarde TEXT,
    klase INTEGER)
'''
)


conn.commit()
conn.close()
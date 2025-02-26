import sqlite3

conn = sqlite3.connect('sql_injection.db')
c = conn.cursor()


inp_username = input('Enter Username: ')
inp_password = input('Enter Password: ')

# query = f"SELECT * FROM user WHERE user.username= '{inp_username}' AND user.password= '{inp_password}';"

with conn:
    # c.execute(query) #negerai
    c.execute("SELECT * FROM user WHERE user.username=? AND user.password=?;", (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print("Jūsų profilio duomenys yra:")
        print(res)
    else:
        print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")


# with conn:
#     c.execute('SELECT * FROM user;')
# print(c.fetchall())

# query = '''CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL,
#     email TEXT NOT NULL
# );
# '''
#
# with conn:
#     c.execute(query)
#
# with conn:
#     c.execute("INSERT INTO user VALUES(NULL, 'adomas', '123456', 'adas@gmail.com');")
#     c.execute("INSERT INTO user(username, password, email) VALUES('tomas', 'asdfgh', 'tomas@gmail.com');")
#     c.execute("INSERT INTO user(username, password, email) VALUES('romas', '987654', 'romas@gmail.com');")


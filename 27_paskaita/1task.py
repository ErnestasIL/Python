import sqlite3

conn = sqlite3.connect("first_task.db")
c = conn.cursor()

query = ''' CREATE TABLE IF NOT EXISTS admin_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT "user"
);
'''
with conn:
    c.execute(query)

inp_username = input('Enter Username: ')
inp_password = input('Enter Password: ')

query = f"SELECT * FROM admin_users WHERE admin_users.username= '{inp_username}' AND admin_users.password= '{inp_password}';"

with conn:
    c.execute(query)
    # c.execute("SELECT * FROM admin_users WHERE admin_users.username= ? AND admin_users.password= ?;", (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print('your login info is:')
        print(res)
    else:
        print('Incorect login or user doesnt exists')


# with conn:
#     c.execute('INSERT INTO admin_users (username, password) VALUES ("bronius69", "654321");')
#     c.execute('INSERT INTO admin_users (username, password) VALUES ("maryte420", "abcdefg");')
#     c.execute('INSERT INTO admin_users (username, password, role) VALUES ("Statyspop", "administratorius" , "admin");')
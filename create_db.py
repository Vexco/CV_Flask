import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

insert = "INSERT INTO message (email, msg) VALUES (?, ?)"

cur = connection.cursor()

cur.execute(insert,('x.xxxx@gmail.com', 'Ceci est un message de xxx, je trouve que votre CV est xxxx'))
cur.execute(insert,('test.test@test.com', 'Cest est un message de test, Je trouve que test'))
cur.execute(insert,('john.doe@outlook.fr', 'Bonjour je suis john doe, j\'aimerais mentretenir avec vous afin de vous parler d\'un poste de développeur'))

connection.commit()
connection.close()
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

insert = "INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)"

cur = connection.cursor()

cur.execute(insert,('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute(insert,('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute(insert,('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute(insert,('TRAMBLEY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute(insert,('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute(insert,('GAGON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute(insert,('DUBOIS', 'Charlotte', '2789, Rue des Roses, 13005 Marseille'))
cur.execute(insert,('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))


connection.commit()
connection.close()
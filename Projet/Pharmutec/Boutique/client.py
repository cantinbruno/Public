#!/usr/bin/env python

import mysql.connector
import socket

db = mysql.connector.connect(
    host="localhost",
    user="dev",
    password="dev",
    database="pharmutec"
)

cursor = db.cursor()

sql_query = "SELECT id, idClient, produits, type_livraison, adresse FROM commande WHERE id=(SELECT max(id) FROM commande) ;"

cursor.execute(sql_query)

result = cursor.fetchall()

payload = ""

i = 0

for data in result[0]:
    if i != 0:
        payload += ',' + str(data)
    else:
        payload += str(data)
    i += 1

host = ("10.17.105.87", 4200)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(host)

sock.send(payload.encode())

sock.close()

import socket
import mysql.connector
import re

db = mysql.connector.connect(
    		host="127.0.0.1",
    		user="dev",
    		password="dev",
    		database="supervision"
		)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.17.105.91', 4200))

while True:
	sock.listen(5)
	client, address = sock.accept()
	result = client.recv(255)
	if result != "":
		result = result.decode('utf-8')
		result = re.sub(r"\s+", "", result)
		print(result)
		cursor = db.cursor()
		sql_query = "INSERT INTO socket (result) VALUES ( '"+result+"' );"
		cursor.execute(sql_query)
		db.commit()
sock.close()

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4200))

while True:
        sock.listen(5)
        client, address = sock.accept()

        result = client.recv(255)
        if result != "":
                print(result.decode('utf-8'))

sock.close()

#!/usr/bin/python3

#Sofia Lopez

import socket

status = 0

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    request = recvSocket.recv(1024).decode("utf-8", "strict")

    slot = request.split(' ')

    try:
    	num = int(slot[1][1:])
    except ValueError:
    	msg = ("Asegurese que su URL contiene un numero al final. Ejemplo: localhost:1234/56")
    	recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body>" + msg + "</body></html>" + "\r\n", 'utf-8'))
    	status = 0

    if status == 0:
    	sum1 = num
    	msg = ("El primer numero es " + str(sum1) + ". Introduzca el segundo numero")
    	status = 1
    	recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body>" + msg + "</body></html>" + "\r\n", 'utf-8'))
    else:
    	sum2 = num
    	total = str(sum1+sum2)
    	msg = str(sum1) + "+" + str(sum2) + "=" + total
    	recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body>" + msg + "</body></html>" + "\r\n", 'utf-8'))
    recvSocket.close()


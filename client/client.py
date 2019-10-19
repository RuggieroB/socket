'''

	# socket

	TPSIT - AS: 2019/20 - Socket (Server e Client)


		Scambio di saluti ed informazioni
		
'''

import socket

import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',10000))

print("\n\nCOMMUNICATION OPENING\n\n\n\n")

s.send(bytes(sys.argv[1],'utf-8'))

data=s.recv(1000)

data=str(data,'utf-8')

print(data)

s.close()

print("\n\n\n\nCOMMUNICATION CLOSING\n\n")

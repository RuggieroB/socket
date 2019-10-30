'''
	
	# socket

		TPSIT - AS: 2019/20 - Socket (Server e Client)


		Scambio di saluti ed informazioni tra Client e Server, finquando il client non chiude la comunicazione.
		
'''

import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',10000))

print("\n\nCOMMUNICATION OPENING\n\n\n\n")

data=s.recv(1000)
data=str(data,'utf-8')

s.send(bytes(sys.argv[1],'utf-8'))

while data != 'STOP' or data != 'CLOSE':

	print(data)
	
	s.send(bytes(sys.argv[1],'utf-8'))
	
	if data == 'STOP' or data == 'CLOSE':
		break 

s.close()

print("\n\n\n\nCOMMUNICATION CLOSING\n\n")

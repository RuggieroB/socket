'''
	
	# socket

		TPSIT - AS: 2019/20 - Socket (Server e Client)


		Scambio di saluti ed informazioni tra Client e Server, finquando il client non chiude la comunicazione.
		
'''

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('',10000))

s.listen(10)

print("\n\nCOMMUNICATION OPENING\n\n")

while True:

	c,a=s.accept()
	
	print("\n\nRiceived comunication from:\t",a,"\n\n")
	
	c.send(bytes('SERVER ACCEPTED COMMUNICATION\n','utf-8'))
	c.send(bytes('COMMUNICATION OPENING','utf-8'))
	
	request=c.recv(1000)
	
	request=str(request,'utf-8')
		
	c.close()

'''
	
	# socket

		TPSIT - AS: 2019/20 - Socket (Server e Client)


		Scambio di saluti ed informazioni tra Client e Server, finquando il client non chiude la comunicazione.
		
'''

import socket
import datetime

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
	
	while request != 'STOP' or request != 'CLOSE':
	
		dt=datetime.datetime.now().isoformat()
		dt_info=dt.split('T')
		d=dt_info[0]
		t=dt_info[1].split('.')[0]
	
		if request == 'Hello!' or request == 'Hello Server!' or request == 'Hi!' or request == 'Hi Server!':
			c.send(bytes('Goodday Client!','utf-8'))
		elif request == 'date':
			c.send(bytes(d,'utf-8'))
		elif request == 'time':
			c.send(bytes(t,'utf-8'))
		elif request == 'datetime':
			dt=datetime.datetime.now().isoformat()
			c.send(bytes(dt,'utf-8'))
		else:
			c.send(bytes('INVALID REQUEST!','utf-8'))
			print("INVALID REQUEST FROM\t",a,"\n\n")
			
	c.send(bytes('\n\nTYPE \"STOP\" OR \"CLOSE\" TO CLOSE COMMUNICATION\n\n','utf-8'))
			
	request=c.recv(1000)	
	request=str(request,'utf-8')
					
	s.send(bytes('\n\n\n\nCOMMUNICATION CLOSING\n\n\n\n','utf-8'))
		
	c.close()
		
print("\n\n\n\nCOMMUNICATION CLOSING\n\n")

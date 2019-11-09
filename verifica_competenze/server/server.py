import socket

import time

import datetime

from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('',10000))

s.listen(10)

clients_list = []

def handleClients():
	global clients_list

	while True:
		print("\n\nClients List is:\t",clients_list)
		time.sleep(0.1)

t=Thread(target=handleClients)
t.start()

print("\n\nCOMMUNICATION OPENING\n\n")

while True:

	c,a=s.accept()
	
	print("\n\nReceived comunication from:\t",a,"\n\n")
	
	request=c.recv(1000)
	request=str(request,'utf-8')
	
	dt=datetime.datetime.now().isoformat()
	dt_info=dt.split('T')
	d=dt_info[0]
	t=dt_info[1].split('.')[0]
	
	while True:
	
		if request == 'Hello!' or request == 'Hello Server!' or request == 'Hi!' or request == 'Hi Server!':
			c.send(bytes('Goodday Client!','utf-8'))
		elif request == 'date':
			c.send(bytes(d,'utf-8'))
		elif request == 'time':
			c.send(bytes(t,'utf-8'))
		elif request == 'datetime':
			dt=datetime.datetime.now().isoformat()
			c.send(bytes(dt,'utf-8'))
		elif request == 'end' or request == 'stop':
			c.close()
			break
		else:
			c.send(bytes('INVALID REQUEST!','utf-8'))
			print("INVALID REQUEST FROM\t",a,"\n\n")
	
		clients_list.append(c)
	
c.close()

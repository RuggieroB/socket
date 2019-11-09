import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',10000))

print("\n\nCOMMUNICATION OPENING\n\n\n\n")

while True:

	request=input("\n>>>:\t")
	request=bytes(request,'utf-8')
	s.send(request)

	data=s.recv(1000)
	data=str(data,'utf-8')
	
	print(data)
	
	if data == 'end' or data == 'stop':
		break

s.close()

print("\n\n\n\nCOMMUNICATION CLOSING\n\n")

import socket			

s = socket.socket()		
print ("Socket successfully created")

port = 12345				

s.bind(('127.0.0.1', port))		
print ("socket binded to %s" %(port))

s.listen()	
print ("socket is listening...")			


c, addr = s.accept()
print ('Got connection from', addr )

data = 'holaloh madrid'
c.send(data.encode())

c.close()

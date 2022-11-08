import socket
import os 
host = 'local host'
port = 5000
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
s.bind(('', port))
s.listen(1)
c, addr = s.accept()

clear = lambda: os.system("cls") 
c.send(b"Welcome Haise \
	Wait for a command")
state = True
while state == True:
	#clear()
	msg = input("Command to send: ")
	
	c.send(msg.encode())
	rec = c.recv(4096)
	print(type(eval(rec.decode('utf-8'))),"\n")

	if msg=="end":
		state = False

# disconnect the server
c.close()

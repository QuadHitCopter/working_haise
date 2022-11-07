import socket

# take the server name and port name
host = 'local host'
port = 5000

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)


# bind the socket with server
# and port number
s.bind(('', port))


# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
c, addr = s.accept()


# display client address
print("CONNECTION FROM:", str(addr))

# send message to the client after
# encoding into binary string
import os 
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

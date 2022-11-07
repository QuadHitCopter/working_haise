from time import sleep
import socket
import os
import pickle
def clear():
	os.system("cls")
  
host = 'local host'
port = 4000

d = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
d.bind(('', port))
  
# allow maximum 1 connection to
# the socket
d.listen(1)

b, addr = d.accept()
name = b.recv(1024).decode("UTF-8")
file = open(f"telem_{name}.txt","w")

count=0
msg = 0
telem_dic = []
while  count<50 and msg!="end":
	


	msg = b.recv(1024)
	try:
		msg = msg.decode('UTF-8')
	except:
		rec = pickle.loads(msg)
		print(rec)
	
	count += 1

d.close()
file.close()
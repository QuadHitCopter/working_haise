from time import sleep
import socket
import os
def clear():
	os.system("cls")
  
host = 'local host'
port = 5000

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
s.bind(('', port))
  
# allow maximum 1 connection to
# the socket
s.listen(1)
  
c, addr = s.accept()
  

  
c.send(b"Init")
sleep(2)
active = True	
command = 0
err = False
sended = False
com_list = ["end", #Finaliza loop de comunicación
	"GET_TM", #Recibir desde sat Telemetría
	"TAKE_PIC",# Tomar foto y enviarla
	"GO_SAFE", #Ir a modo seguro
	"RECOVER", #Volver a modo Normal
	"ALL_OK" #Estado de sensores OK
	] 
while  active == True and command !="end":
	clear()
	if err:
		print(f"Comando erroneo: {command} . . . \n")
	elif sended:
		print(f"Comando Enviado: {command} . . . \n")
	command = input("Comando: ")
	if command in com_list:
		c.send(command.encode())
		err  =False
		sended = True
		
	else:
		err = True		
		sended = False
	sleep(0.5)
  

c.close()
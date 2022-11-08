from time import sleep
import socket
import os
import json
import copy
def clear():
	os.system("cls")

##########
"""Inicia lectura de JSON para guardar el com_num inicial"""
a=True
while a:
	try :
		with open("command_now.json", "r") as file:
			command_state_old = json.load(file)
			com_num_old  = command_state_old["com_num"]
			a = False
	except:
		pass
##################################
"""Inicia server para comunicaciones con el cliente"""

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

###################################
sleep(2) #espera dos segundos 


com_list = ["end", #Finaliza loop de comunicación
	"GET_TM", #Recibir desde sat Telemetría
	"TAKE_PIC",# Tomar foto y enviarla
	"GO_SAFE", #Ir a modo seguro
	"RECOVER", #Volver a modo Normal
	"ALL_OK" #Estado de sensores OK
	] 

#########################################
"""Espera por cambios en el JSON para enviar dicho comando"""
a = True
sended = False
err = False

while a:
	clear()
	#if sended:
	#	print("Ultimo telecomando enviado:", command)
	##Verifica cambios en JSON
	try :
		with open("command_now.json", "r") as file:
			command_state = json.load(file)
			command  = command_state["command"]
			com_num  = command_state["com_num"]
			sleep(0.02)
			if (com_num_old != com_num) and (command !="end"):
				com_num_old = copy.deepcopy(com_num)
				c.send(command.encode())
				sended = True
			elif (com_num_old != com_num) and (command =="end"):
				c.send(command.encode())
				a = False
				#print("Sesión terminada")
				sended = True
			else: 
				sended = True
	except:
		a= True


c.close()
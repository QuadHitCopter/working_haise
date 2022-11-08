import os
from datetime import datetime
from time import sleep
import json


def clear():
	os.system("cls")
def com_updating(com,t,N):
	dict = {"com_num":N,"command":com,"com_date":t}

	json_dic = json.dumps(dict,indent=1)

	with open("command_now.json","w") as update:
	
		update.write(json_dic)
	with open("command_hist.txt","a") as hist:
		hist.write(str(dict) + "\n")	
	return dict

try:
	with open("command_hist.txt", "rb") as file:
		try:
			file.seek(-2, os.SEEK_END)
			while file.read(1) != b'\n':
				file.seek(-2, os.SEEK_CUR)
		except OSError:
	        	file.seek(0)
		last_line = file.readline().decode("UTF-8")
		
		alpha = json.loads(last_line.__str__().replace("'",'"'))
		N = alpha["com_num"]
		
		
except OSError:
	print(OSError)
	N=0




com_updating("Init",str(datetime.now())[0:-4],N)


active = True
command = 0
err = False
saved = False

com_list = ["end", #Finaliza loop de ingreso de comandos
	"GET_TM", #Recibir desde sat Telemetría
	"TAKE_PIC",# Tomar foto y enviarla
	"GO_SAFE", #Ir a modo seguro y reinicia contador de telecomandos
	"RECOVER", #Volver a modo Normal
	"ALL_OK", #Estado de sensores OK
	] 


while command !="end":
	clear()
	if err:
		print(f"Comando erroneo: {command} . . . \n")
	elif saved:
		print(f"Comando Enviado:", dictio)
	command = input("Comando: ")
	
	if command in com_list:	
		if command == "GO_SAFE":
			N = 0
		else:
			N = N + 1
		t = str(datetime.now())[0:-4]
		dictio = com_updating(command,t,N)

		err = False

		saved = True
		
	else:
		err = True		
		saved = False
	sleep(0.04)
  
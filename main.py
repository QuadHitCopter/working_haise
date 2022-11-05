import socket
from time import sleep
from power import measure
import os
from random import randint

clear = lambda: os.system("clear")
clear()

class sat:
	def __init__(self,state,bat,v5,cam,adc):
		self.state = state
		self.bat_state = bat
		self.v5_state = v5
		self.cam_state = cam
		self.adc_state = adc
haise = sat("NORMAL","OK","OK","OK","OK")


host = 'local host'
port = 5000

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

#
ff = True
bb = 0
def check(ss):
	try:
		ss.getpeername()
		return False
	except:
		return True

while ff == True:
	try:
		s.connect(('192.168.0.12', port))
	except:
		bb = bb+1
		print(f"Fallo n°{bb}")
		sleep(1)
		s.close
		s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

	ff= check(s)
s.settimeout(None)

#s.connect(('192.168.0.12', port))
#s.settimeout(None)
#print(s.getpeername())
#sleep(10)
def change():
	haise.bat_state = "OK"
	haise.v5_state = "OK"
	haise.cam_state = "OK"
	haise.adc_state = "OK"
#msg = s.recv(1024)


loop = True
clear()
msg = True

while loop == True and msg:

	sleep(0.05)
	#print('Received:' + com)

	print(f"Mode:{haise.state}||BAT: {haise.bat_state}||V5: {haise.v5_state}||CAM: {haise.cam_state}||ADCs:{haise.adc_state}")
	sleep(0.05)
	msg = s.recv(1024)
	sleep(0.05)

	com = msg.decode()

	if com == "end":
		loop = False
	elif com == "GO_SAFE":
		clear()


		haise.bat_state = "NOK"
		haise.v5_state = "NOK"
		haise.cam_state = "NOK"
		haise.adc_state = "NOK"





	elif com == "RECOVER":

		if haise.state == "SAFE_MODE":

			if  haise.bat_state == "OK" and haise.v5_state == "OK" and haise.cam_state == "OK" and haise.adc_state == "OK" :
				clear()
				haise.state = "NORMAL"

			else:
				clear()

	elif com == "TAKE_PIC" and haise.state == "NORMAL":
		clear()
		e = 0
		for tt in range(4):
			sleep(0.3)
			print(".")
			d = randint(0,100)
			if d>10 and d < 20:
				e = 1
				haise.cam_state = "NOK"
				if d > 12 and d < 15:
					haise.bat_state = "NOK"
		if e!=1:
			print("FOTO TOMADA")

	#COMANDOS OK
	elif com == "GET_V":
		clear()
		measure(2,0.1,"main","w")


	elif com == "BAT_OK":
		haise.bat_state = "OK"
		clear()
	elif com == "V5_OK":
		haise.v5_state = "OK"
		clear()
	elif com == "CAM_OK":
		haise.cam_state = "OK"
		clear()
	elif com == "ADC_OK":
		haise.adc_state = "OK"
		clear()
	elif com == "ALL_OK":
		change()
	if "NOK" in haise.__dict__.values():
		haise.state = "SAFE_MODE"



	sleep(0.2)



s.close()

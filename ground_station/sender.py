from time import sleep
import json
import copy
a = True
while a:
	try :
		with open("command_now.json", "r") as file:
			command_state_old = json.load(file)
			com_num_old  = command_state_old["com_num"]
			a = False
	except:
		pass
a = True
while a:
	try :
		with open("command_now.json", "r") as file:
			command_state = json.load(file)
			command  = command_state["command"]
			com_num  = command_state["com_num"]
			sleep(0.02)
			if (com_num_old != com_num) and (command !="end"):
				com_num_old = copy.deepcopy(com_num)
				print("num_com: ", com_num)
			elif (com_num_old != com_num) and (command =="end"):
				a = False
				print("Sesión terminada")
	except:
		a= True
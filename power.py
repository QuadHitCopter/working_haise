from ina219 import INA219
from ina219 import DeviceRangeError
import time
from time import sleep
import csv
from datetime import datetime
import subprocess


def read(ina):
	b_v = ina.voltage()
	try:
		b_c = ina.current()
		b_p = ina.power()
	except DeviceRangeError as e:
		print(e)
	return b_v, b_c, b_p

def measure(Dt,h,name,mode):
	"""
	Dt,h,filename,mode (w,a)
	"""

	SHUNT_OHMS = 0.1
	max_AMP = 1.0
	ad5v = 0x45
	adbat = 0x40


	ina_5v = INA219(SHUNT_OHMS,max_AMP,address=ad5v)
	ina_5v.configure(ina_5v.RANGE_16V)
	ina_bat = INA219(SHUNT_OHMS,max_AMP,address=adbat)
	ina_bat.configure(ina_bat.RANGE_16V)





	dat = open(f"./data/power_data_{name}.csv",mode)
	writer = csv.writer(dat)
	if mode == "w":
		header = ["time","5V voltage [V]","5V current [mA]", "5V power [mW]","Bat Voltage [V]","Bat Current [mA]", "Bat Power [mW]"]
		writer.writerow(header)


	t = []
	V_all = []
	I_all = []

	for tt in range(int(Dt//h)):
		time.sleep(h)
		#     tim = tt*0.01
		timez = datetime.now().time()

		#     t.append(tim)
		V5_line = read(ina_5v)
		bat_line =read(ina_bat)
		v5 = V5_line[0]
		v5_i = V5_line[1]
		v5_p = V5_line[2]
		bat_v = bat_line[0]
		bat_i = bat_line[1]
		bat_p = bat_line[2]

		linea = [timez,f"{v5:.3f}",f"{v5_i:.5f}",f"{v5_p:.4f}",f"{bat_v:.3f}",f"{bat_i:.5f}",f"{bat_p:.4f}"]
		writer.writerow(linea)
		print(linea)
	dat.close()





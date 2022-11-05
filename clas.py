from time import sleep
class haise:
	def __init__(self, state):
		self.state = state
haise_sat = haise("IDLE")
print(haise_sat.state)
sleep(0.5)
haise_sat.state = "SAFE_MODE"
print(haise_sat.state)

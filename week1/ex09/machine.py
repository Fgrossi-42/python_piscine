import random

from beverages import *

class CoffeeMachine:
	def __init__(self):
		self.count = 9
		self.isworking = True
		self.beverages = [Cappuccino(), Coffee(), Tea(), Chocolate(), Dan()]

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90
		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __str__(self):
			return "This coffee machine has to be repaired."

	def repair(self):
		self.isworking = True
		self.count = 0

	def serve(self, ch):

		if self.count == 10 or self.isworking is False:
			self.isworking = False
			raise self.BrokenMachineException

		self.count += 1
		if random.choice([range(0, 6)]) != 0:
			for x in self.beverages:
				if x.name == ch:
					return x
		return (self.EmptyCup())

def main():
	machine = CoffeeMachine()
	while 1:
		v = input("Scegliere la bevanda: ")
		if v == "repair":
			machine.repair()
		else:
			try:
				print(machine.serve(v).description())
			except Exception as e:
				print(e)

if __name__ == "__main__":
	main()

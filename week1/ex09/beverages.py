class HotBeverage:
	price = .30
	name = "hot beverage"

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		return f"name : {self.name}\nprice : {format(self.price, '.2f')}\ndescription : {self.description()}"

class Coffee(HotBeverage):
	name = "Coffee"
	price = 0.40

	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "Tea"

class Chocolate(HotBeverage):
	name = "Chocolate"
	price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	name = "Cappuccino"
	price = 0.45

	def description(self):
		return "Un po' di Italia nella sua tazza!"

class Dan(HotBeverage):
	name = "Dan"
	price = 0.00

	def description(self):
		return "Un Dan selvatico vuole combattere"

if __name__ == "__main__":
	print(HotBeverage(), '\n', sep='')
	print(Coffee(), '\n', sep='')
	print(Tea(), '\n', sep='')
	print(Chocolate(), '\n', sep='')
	print(Cappuccino())

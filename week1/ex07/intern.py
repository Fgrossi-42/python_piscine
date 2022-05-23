class Intern:

	def __init__(self, name=None):
		if name != None:
			self.name = name
		else:
			self.name = "My name? I'm nobody, an intern, I have no name."

	def __str__(self):
		return f"{self.name}"

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return self.Coffee()


def test():

	pers1 = Intern()
	pers2 = Intern("Mark")
	print(f"{pers2.name} : ")
	print(pers2.make_coffee())

	print(f"{pers1.name} : ")
	try:
		pers1.work()
	except Exception as error:
		print(error)

if __name__ == '__main__':
	test()

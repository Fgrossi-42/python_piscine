import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def main(argv: list):
	if len(argv) == 2:
		if argv[1] in states:
			state = states[argv[1]]
			print(capital_cities[state])
		else:
			print("Unknown state")

main(sys.argv)

from logging import captureWarnings
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
		for key, value in capital_cities.items():
			if argv[1] == value:
				for key2, value2 in states.items():
					if key == value2:
						print(key2)
						return
		print("Unknown state")

main(sys.argv)

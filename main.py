import os
from parser import *
from regex import *

def main():
	try:
		inputname = input("computor ")

		parse_input(inputname)
		# assert term_to_dict(["+5*X^0","+4*X^1","-9.3*X^2"]) == {0: 5.0, 1: 4.0, 2: -9.3}
		# assert term_to_dict(["+2*X^1","+3*X^1","-5*X^1"]) == {}  # 0 net → pruned
	except ValueError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()

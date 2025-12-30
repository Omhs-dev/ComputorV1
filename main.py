import os
from parser import *
from regex import *
from polynomial import *

def main():
	try:
		inputname = input("computor ")

		l_dict, r_dict = parse_input(inputname)
		# print(f"left dict: {l_dict}")
		# print(f"right dict: {r_dict}")
		reduce_equation(l_dict, r_dict)
	except ValueError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()

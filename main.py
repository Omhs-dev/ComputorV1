import os
from parse import *
from regex import *

def main():
	try:
		inputname = input("computor ")

		parse_input(inputname)
	except ValueError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()

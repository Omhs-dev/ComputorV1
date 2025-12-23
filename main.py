import os
from parse import *

def main():
	try:
		inputname = input("computor ")

		l, r = normalize_equation(inputname)
		print(f"left: {l} and right: {r}")
		# parse_side(inputname)
	except ValueError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()

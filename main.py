import os
from parse import *

def main():
	inputname = input("computor ")

	l, r = pre_normalize(inputname)
	print(f"left: {l} and right: {r}")
	# parse_side(inputname)

if __name__ == "__main__":
	main()

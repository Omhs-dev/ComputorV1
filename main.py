import os

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

# Input has to be in ""
# Input must have only: Numbers(Int, float), *, X, +, -, ^ and =

def parse_side(str):
	'''
		Parse equation into two side
		l_side and r_side
	'''
	try:
		print()
	except TypeError:
		return None

# def reduce_equation(l_side, r_side)

def main():
	inputname = input("computor ")

	if (inputname == "one"):
		print("this is a number")

if __name__ == "__main__":
	main()

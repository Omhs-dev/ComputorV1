# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

# Input has to be in ""
# Input must have only: Numbers(Int, float), *, X, +, -, ^ and =

def normalize_equation(i_str):
	if i_str == "":
		print("The string is empty.")
		return None
	str_nor = i_str.replace(" ", "")
	try:
		l_side, r_side = str_nor.split("=")
	except ValueError:
		raise ValueError("Equation must contain one '=' symbol")
	if l_side == "" or r_side == "":
		raise ValueError("Both Sides must be non-empty")
	if l_side[0] not in "+-":
		# print("Warning: does not have a sign")
		l_side = "+" + l_side
	if r_side[0] not in "+-":
		# print("Warning: does not have a sign")
		r_side = "+" + r_side
	return l_side, r_side

def parse_side(str):
	'''
		Parse equation into two side
		l_side and r_side
	'''
	try:
		if str == "":
			print("The string is empty.")
	except TypeError:
		return None

# def reduce_equation(l_side, r_side)

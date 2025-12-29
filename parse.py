from regex import *

# 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0

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

def all_terms_components(raw_terms):
	i = 0
	for term in raw_terms:
		print(f"terms {i}: {term}")
		sign, const, exponent = extract_term_components(term)
		print(f"sign: {sign}")
		print(f"const: {const}")
		print(f"exponent: {exponent}")
		i+=1
	return sign, const, exponent

def parse_input(i_str):
	'''
		Parse equation into two side
		l_side and r_side
	'''
	if not i_str:
		raise ValueError("String is empty")

	l_side, r_side = normalize_equation(i_str)
	# print(f"left: {l_side} and right: {r_side}")

	l_raw_terms = extract_raw_terms(l_side)
	r_raw_terms =extract_raw_terms(r_side)

	all_terms_components(l_raw_terms)
	all_terms_components(r_raw_terms)

# def reduce_equation(l_side, r_side)

# init constanat and exponential into float and digit
def normalize_term(const, exp):
	n_const = float(const)
	n_exp = int(exp)
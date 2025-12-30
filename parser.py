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

def term_to_dict(raw_terms):
	d = {}
	for term in raw_terms:
		print(f"terms : {term}")
		components = extract_term_components(term)
		if not components:
			continue

		sign, coef_s, exp_s = components 
		if sign == '+':
			coef = float(coef_s) * 1.0
		else:
			coef = float(coef_s) * -1.0
		exp = int(exp_s)
		d[exp] = d.get(exp, 0.0) + coef
	eps = 1e-12 #epsilon
	return {e: c for e, c in d.items() if abs(c) > eps}

def parse_input(i_str):
	'''
		Parse equation into two side
		l_side and r_side
	'''
	if not i_str:
		raise ValueError("String is empty")

	l_side, r_side = normalize_equation(i_str)

	l_raw_terms = extract_raw_terms(l_side)
	r_raw_terms =extract_raw_terms(r_side)

	l_dict = term_to_dict(l_raw_terms)
	r_dict = term_to_dict(r_raw_terms)

	return l_dict, r_dict

# def reduce_equation(l_side, r_side)

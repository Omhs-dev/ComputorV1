from parser import *

def format_number(n):
	if n.is_integer():
		return str(int(n))
	return str(n)


def display_reduced_form(red_dict):
	expression = ""
	first_term = True
	sorted_terms = dict(sorted(red_dict.items()))

	for exp, coef in sorted_terms.items():
		if abs(coef) < 1e-12:
			continue
		sign = "+" if coef >= 0 else "-"
		abs_coef = format_number(abs(coef))
		term = f"{abs_coef} * X^{exp}"

		if first_term:
			expression += term
			first_term = False
		else:
			expression += f" {sign} {term}"

	expression += " = 0"
	# print(expression)
	return expression

def reduce_equation(left, right):
	'''
	Docstring for reduce_equation

	move everything to the left
	check the matching exponent
	calculate the matching ones
	then equalize everything to 0
	then return
	'''
	# matching exponent is given once
	all_exp = set(left) | set(right)

	for exp in all_exp:
		l = left.get(exp, 0.0)
		r = right.get(exp, 0.0)
		coef = l - r
		if abs(coef) > 1e-12:
			left[exp] = round(coef, 12)
	# print(f"\nupdated left dict: {left}")
	
	return left

def detect_degree(red_form):
	exp = set(red_form)
	degree = max(exp)
	print(f"degree: {degree}")
	return degree

left_dict = {0: 5.3, 1: -4.0, 3: 0.0}
right_dict = {0: 4.0}

red = reduce_equation(left_dict, right_dict)

detect_degree(red)

from parser import *

def display_reduce_form(red):
	print("reduced form")
	# sort terms by exp
	# displaying all terms including 0 coef
	# usr +/- form
	# end with = 0

	red_eq = []
	reduced_form = ""
	sorted_terms = dict(sorted(red.items()))
	print(sorted_terms)

	# skip the first item for sign assignement

	for key, value in sorted_terms.items():
		first_term = next(iter(sorted_terms))
		sign = "+" if value >= 0 else ""
		term = f"{sign}{value} * X^{key}"
		red_eq.append(term)
	
	for term in red_eq:
		# if term[0]:
		# 	term.replace("+", "")
		reduced_form = reduced_form + " " + term + " "

	print(red_eq)
	print(reduced_form)

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

left_dict = {0: 5.3, 1: -4.0, 3: 0.0}
right_dict = {0: 4.0}

red = reduce_equation(left_dict, right_dict)

display_reduce_form(red)
from parser import *

def display_reduce_form(red):
	print("reduced form")
	# sort terms by exp
	# displaying all terms including 0 coef
	# usr +/- form
	# end with = 0

	expression = ""
	terms_list = []
	sorted_terms = dict(sorted(red.items()))
	print(sorted_terms)

	# skip the first item for sign assignement

	for key, value in sorted_terms.items():
		#remove every value sign "+" and "-"
		# first_term = next(iter(sorted_terms))
		print(f"value: {value}")
		sign = "+" if value >= 0 else "-"
		term = f"{value} * X^{key}"
		unsigned_term = term if value >= 0 else term.replace("-", "")
		terms_list.append((sign, unsigned_term))
		print("here")

	for i, (sign, term) in enumerate(terms_list):
		if term.startswith("0.0"):
			continue
		expression += term if i == 0 and sign == "+" else f" {sign} {term}"
	# make a dict of terms key = sign and value = term
	print(terms_list)
	expression += " = 0"
	print(expression)
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

left_dict = {0: 5.3, 1: -4.0, 3: 0.0}
right_dict = {0: 4.0}

red = reduce_equation(left_dict, right_dict)

display_reduce_form(red)
from parser import *

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

# left_dict = {0: 5.3, 1: 4.0, 3: 5.0}
# right_dict = {0: 4.0}

# reduce_equation(left_dict, right_dict)

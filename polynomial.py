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

	print(f"left dict: {left}")
	print(f"right dict: {right}")

	# here each matching exponent is given once because for the union
	all_exp = set(left) | set(right)

	print(f"all exp: {all_exp}")
	for exp in all_exp:
		l = left.get(exp, 0.0)
		r = right.get(exp, 0.0)
		print(f"For key: {exp} -> left: {l}, right: {r}")
		coef = l - r
		
		if abs(coef) > 1e-12:
			left[exp] = round(coef, 12)
			print(f"Right side goes to the left -> l - r: {l}")
	print(f"\nupdated left dict: {left}")
	return left

left_dict = {0: 5.3, 1: 4.0, 3: 5.0}
right_dict = {0: 4.0}

reduce_equation(left_dict, right_dict)

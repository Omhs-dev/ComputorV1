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

	# l_keys = left.keys()
	# r_keys = right.keys()

	# print(f"keys l: {l_keys}")
	# print(f"keys r: {r_keys}")

	# here each matching exponent is given once because for the union
	all_exp = set(left) | set(right)

	print(f"all exp: {all_exp}")
	for exp in all_exp:
		l = left.get(exp)
		r = right.get(exp)
		print(f"For key: {exp} -> left: {l}, right: {r}")

		if l != None and r != None:
			l-=r
			print(f"Right side goes to the left -> l - r: {l}")

left_dict = {0: 5.0, 1: 4.0, 3: 5.0}
right_dict = {0: 4.0}

reduce_equation(left_dict, right_dict)

import math
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

def get_degree(red_form):
	exp = set(red_form)
	degree = max(exp)
	return degree

def solve_degree_0(red_form):
	a = red_form.get(0,0)
	print(a)

def solve_degree_1(red_form):
	# f(x) = ax + b
	# x = - (b/q) 

	a = red_form.get(1, 0)
	b = red_form.get(0, 0)
	x = -b / a

	print(f"solution: {x}")
	return x

def solve_degree_2(red_form):
	# f(x) = ax^2 + bx + c
	# delta = b^2 - 4ac

	a = red_form.get(2, 0)
	b = red_form.get(1, 0)
	c = red_form.get(0, 0)

	print(f"a: {a} - b: {b} - c: {c}")

	delta = b**2 - 4 * a * c

	if delta > 0:
		print("2 solutions: ")
		x_1 = (-b + math.sqrt(delta)) / (2 * a)
		x_2 = (-b - math.sqrt(delta)) / (2 * a)
		print(f"x1: {x_1} and x2: {x_2}")
	if delta == 0:
		print("only 1 solution exist: ")
		x = -b / 2 * a
		print(f"x: {x}")
	if delta < 0:
		print("The polynomial has no real solutions")
	print(delta)

def solve_polynomial(degree, red_form):
	print("poly")
	print(degree)
	print(red_form)
	if degree == 0:
		print("Every real number is a solution")
		# solve_degree_1
	if degree == 1:
		print("The solution is:")
		solve_degree_1(red_form)
	if degree == 2:
		print("Discriminant is strictly positive, the two solutions are:")
		solve_degree_2(red_form)
	if degree > 2:
		print("The polynomial degree is strictly greater than 2, I can't solve.")

# 2x^2−4x−6
# x2−4x+4=0

# left_dict = {0: -6, 1: -4, 2: 2}
left_dict = {0: 4, 1: -4, 2: 1}
right_dict = {0: 4.0}

# red = reduce_equation(left_dict, right_dict)
# deg = get_degree(red)
# solve_polynomial(deg, red)

solve_degree_2(left_dict)

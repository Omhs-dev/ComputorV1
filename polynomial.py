import math
from parser import *

def format_number(n):
	if n.is_integer():
		return str(int(n))
	return str(n)

def format_reduced_form(red_dict):
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
	return int(degree)

def solve_degree_0(red_form):
	a = red_form.get(0,0)

	if a != 0:
		print("No solution")
	if a == 0:
		print("All real numbers are solutions")
	# print(a)
	# return a

def solve_degree_1(red_form):
	# f(x) = ax + b
	# x = - (b/q) 

	a = red_form.get(1, 0)
	b = red_form.get(0, 0)
	x = -b / a

	print(f"The solution is:\n{x}")
	# return x

def solve_degree_2(red_form):
	# f(x) = ax^2 + bx + c
	# delta = b^2 - 4ac

	a = red_form.get(2, 0)
	b = red_form.get(1, 0)
	c = red_form.get(0, 0)

	delta = b**2 - 4 * a * c

	if delta > 0:
		x_1 = (-b - math.sqrt(delta)) / (2 * a)
		x_2 = (-b + math.sqrt(delta)) / (2 * a)
		print("Discriminant is strictly positive, the two solutions are:")
		print(f"x1: {x_1:.6}\nx2: {x_2:.6}")
		# return x_1, x_2
	if delta == 0:
		x = -b / 2 * a
		print("Discriminant is = 0, the solution is:")
		print(f"x: {x}")
		# return x
	if delta < 0:
		print("Discriminant is strictly negative, no real solutions")
	return None

def solve_polynomial(red_form, degree):
	if degree == 0:
		solve_degree_0(red_form)
	if degree == 1:
		solve_degree_1(red_form)
	if degree == 2:
		solve_degree_2(red_form)
	if degree > 2:
		print("The polynomial degree is strictly greater than 2, I can't solve.")

# 2x^2−4x−6
# x2−4x+4=0

# left_dict = {0: -6, 1: -4, 2: 2}
left_dict = {0: 4, 1: -4, 2: 1}
right_dict = {1: 4.0}

red = reduce_equation(left_dict, right_dict)
deg = get_degree(red)

print(f"Degree: {deg}")
# solve_polynomial(deg, red)

solve_polynomial(red, deg)

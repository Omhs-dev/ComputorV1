from src.utils import *

def format_reduced_form(red_dict):
	expression = ""
	first_term = True
	sorted_terms = dict(sorted(red_dict.items()))

	if is_zero_polynomial(red_dict):
		expression = "0 = 0"
		return expression
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
	return expression

def reduce_equation(left, right):
	'''
	move everything to the left
	check the matching exponent
	calculate the matching ones
	then equalize everything to 0
	then return
	'''
	all_exp = set(left) | set(right)

	for exp in all_exp:
		l = left.get(exp, 0.0)
		r = right.get(exp, 0.0)
		coef = l - r
		if abs(coef) > 1e-12:
			left[exp] = round(coef, 12)
		else:
			left[exp] = 0
	return left

def get_degree(red_form):
	exp = set(red_form)
	if not red_form:
		return 0
	degree = max(exp)
	return int(degree)

#TODO: Implement a function called intermediate_steps

def solve_degree_0(red_form):
	a = red_form.get(0,0)

	if a != 0:
		print("No solution")
	if a == 0:
		print("All real numbers are solutions")

def solve_degree_1(red_form):
	'''	
	f(x) = ax + b
	x = - (b/q)
	'''
	a = red_form.get(1, 0)
	b = red_form.get(0, 0)
	x = -b / a
	print("\nSteps:\n")
	print(f"a = {a}\nb = {b}\n")
	print(f"x = -b / a")
	print(f"x = {format_number(-b)} / {format_number(a)}")
	print(f"x = {format_number(x)}\n")
	print(f"The solution is:\n{format_number(x)}")

def solve_degree_2(red_form):
	'''
	f(x) = ax^2 + bx + c
	delta = b^2 - 4ac
	'''
	if is_zero_polynomial(red_form):
		print("All real numbers are solutions")
		return None

	a = red_form.get(2, 0)
	b = red_form.get(1, 0)
	c = red_form.get(0, 0)

	delta = b**2 - 4 * a * c

	if delta > 0:
		x_1 = (-b - sqrt_newton(delta)) / (2 * a)
		x_2 = (-b + sqrt_newton(delta)) / (2 * a)
		print(positive_delta_steps(delta, a, b, c).strip())
		print_two_real_solutions(x_1, x_2)
	if delta == 0:
		x = -b / 2 * a
		print_one_real_solution(x)
	if delta < 0:
		alpha_1 = -b / (2 * a)
		beta_1 = sqrt_newton(abs(delta)) / (2 * a)
		alpha_2 = -b / (2 * a)
		beta_2 = sqrt_newton(abs(delta)) / (2 * a)
		print_two_complex_solutions(alpha_1, beta_1, alpha_2, beta_2)

def solve_polynomial(red_form, degree):
	if degree == 0:
		solve_degree_0(red_form)
	if degree == 1:
		solve_degree_1(red_form)
	if degree == 2:
		solve_degree_2(red_form)
	if degree > 2:
		print_degree_limit_error()

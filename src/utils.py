import re

def print_discriminant_positive(x_1, x_2):
	print("Discriminant is strictly positive, the two solutions are:")
	print(f"{x_1:.6}\n{x_2:.6}")

def print_discriminant_zero(x):
	print("Discriminant is = 0, the solution is:")
	print(f"x: {format_number(x)}")

def print_discriminant_negative():
	print("Discriminant is strictly negative, no real solutions")

def print_degree_limit_error():
	print("The polynomial degree is strictly greater than 2, I can't solve.")

def print_reduced_form(red_form):
	print(f"Reduced form: {red_form}")

def print_degree(degree):
	print(f"Polynomial degree: {degree}")

def is_X_only(i_str):
	'''verify that only X is being used as variable'''
	for ch in i_str:
		if ch.isalpha() and ch != "X":
			return False
	return True

def is_valid_term(term):
	'''check if a term is valid (-|=d * X^n)'''
	n_term = term.replace(" ", "")
	valid_term = re.fullmatch(r"^[-+]?[0-9]+(:?\.[0-9]+)?\*X\^[0-9]+?$", n_term)

	if valid_term is not None:
		return True
	return False

def check_bad_spacing(i_str):
	'''
	check if there are spaces around exponent symbol '^'
	verify if '-' and '+' are consecutive '-+'
	check if there are no spaces around '=' and '*'
	skip sign at the begining of the string and after each '= '
	then verify if there are no spaces around '-' and '+'
	'''
	if re.search(r"\s\^|\^\s", i_str):
		return True
	if re.search(r"(:?\-\s*\+|\+\s*\-)", i_str):
		return True
	if re.search(r"(?<! )[=*]|[=*](?! )", i_str):
		return True
	if re.search(r"(:?(?<!^)(?<!= ))(:?(?<! )[-+]|[-+](?! ))", i_str):
		return True
	return False

def format_number(n):
	if n.is_integer():
		return str(int(n))
	return str(n)

def sqrt_newton(x):
	'''
	Newton formula:
	n_guess = n_guess - f(curr_guess)/f'(curr_guess)
	
	for my square root implementation:
	y^2 = x
	f(y) = y^2 - x
	f'(y) = 2y
	y_new = y - f(y) / f'(y)
	'''

	if x < 0:
		raise ValueError("Can not compute negative numbers")
	if x == 0:
		return 0
	if x == 1:
		return 1
	
	y = x/2 if x >= 1 else 1 # the guess

	i = 0
	while abs(y**2 - x) / x > 1e-12 and i < 50:
		y_new = 1/2 * (y + (x/y))
		y = y_new
		i = i + 1
	return y
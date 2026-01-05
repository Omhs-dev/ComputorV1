import re

def print_degree_limit_error():
	print("The polynomial degree is strictly greater than 2, I can't solve.")

def print_reduced_form(red_form):
	print(f"Reduced form: {red_form}")

def print_degree(degree):
	print(f"Polynomial degree: {degree}")

def format_number(n):
	if n.is_integer():
		return str(int(n))
	return str(n)

def is_X_only(i_str):
	for ch in i_str:
		if ch.isalpha() and ch != "X":
			return False
	return True

def is_valid_term(term):
	n_term = term.replace(" ", "")
	valid_term = re.fullmatch(r"^[-+]?[0-9]+(:?\.[0-9]+)?\*X\^[0-9]+?$", n_term)

	if valid_term is not None:
		return True
	return False

def check_bad_spacing(i_str):
	bad_spacing = re.search(r"(?<! )[-+=*]|[-+=*](?! )", i_str)

	if re.search(r"(?<! )[-+=*]|[-+=*](?! )", i_str):
		return True
	if re.search(r"\s\^|\^\s", i_str):
		return True
	return False

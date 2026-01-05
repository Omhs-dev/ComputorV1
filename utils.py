import re

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

	if bad_spacing:
		return True
	return False

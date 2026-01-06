import re
from src.utils import *

def extract_raw_terms(n_str):
	if not n_str:
		return []
	terms = re.findall(r"[+-][^+-]+", n_str)

	for term in terms:
		if not is_valid_term(term):
			raise ValueError(f"Incorrect term: {term}")
	return terms

def extract_term_components(term):
	match = re.match(r"^([-+])([0-9]+(?:\.[0-9]+)?)\*X(?:\^([0-9]+))?$", term)

	if not match:
		return None
	sign, const, exp = match.groups()
	return sign, const, exp

def parse_only_constant(term):
	match = re.match(r"^([-+])([0-9]+(?:\.[0-9]+)?)$", term)

	if not match:
		return None
	exp = 1
	sign, const = match.groups()
	return sign, const, exp

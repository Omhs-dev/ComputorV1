import os
from parse import *
from regex import *

def main():
	try:
		inputname = input("computor ")

		l_side, r_side = normalize_equation(inputname)
		print(f"left: {l_side} and right: {r_side}")

		i = 0
		for term in extract_raw_terms(l_side):
			print(f"terms {i}: {term}")
			singed_coef, exponent = extract_term_components(term)
			print(f"singed_coef: {singed_coef}")
			print(f"exponent: {exponent}")
			i+=1
	except ValueError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()

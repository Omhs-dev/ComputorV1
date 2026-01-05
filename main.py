import os
from parsing import *
from regex import *
from polynomial import *

# 5 * X^0 + 4 * X^1 - 0 * X^2 = 1 * X^0

def main():
	try:
		inputname = input("computor ")

		l_dict, r_dict = parse_input(inputname)
		# print(f"left dict: {l_dict}")
		# print(f"right dict: {r_dict}")
		reduced_form = reduce_equation(l_dict, r_dict)
		display_form = format_reduced_form(reduced_form)
		degree = get_degree(reduced_form)

		# TODO: Implement a printer for reduced_form
		print(f"Reduced form: {display_form}")
		print(f"Polynomial degree: {degree}")

		solve_polynomial(reduced_form, degree)
	except ValueError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()

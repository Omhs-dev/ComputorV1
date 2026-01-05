import os

from parsing import parse_input
from utils import print_reduced_form, print_degree
from polynomial import (
	reduce_equation,
	format_reduced_form,
	get_degree,
	solve_polynomial,
)

# 5 * X^0 + 4 * X^1 - 0 * X^2 = 1 * X^0

def main():
	try:
		inputname = input("computor ")

		l_dict, r_dict = parse_input(inputname)
		reduced_form = reduce_equation(l_dict, r_dict)
		display_form = format_reduced_form(reduced_form)
		degree = get_degree(reduced_form)
		print_reduced_form(display_form)
		print_degree(degree)
		solve_polynomial(reduced_form, degree)
	except ValueError as e:
		print(f"Error: {e}")
	except (KeyboardInterrupt, EOFError):
		print("\nExiting...")

if __name__ == "__main__":
	main()

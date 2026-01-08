import os

from src.parsing import parse_input
from src.utils import print_reduced_form, print_degree
from src.polynomial import (
	reduce_equation,
	format_reduced_form,
	get_degree,
	solve_polynomial,
)

# 5 * X^0 = 5 * X^0
# 4 * X^0 = 8 * X^0
# 5 * X^0 = 4 * X^0 + 7 * X^1
# 5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1
# 6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1
# 5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1

# TODO: clean terminal after each input
def main():
	try:
		input_poly = input("computor ")

		l_dict, r_dict = parse_input(input_poly)
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

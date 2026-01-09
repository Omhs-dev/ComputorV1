import sys

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

def main():
	try:
		if len(sys.argv) != 2:
			print("Error: please provide the equation")
			return 1

		input_poly = sys.argv[1]

		l_dict, r_dict = parse_input(input_poly)
		reduced_form = reduce_equation(l_dict, r_dict)
		display_form = format_reduced_form(reduced_form)
		degree = get_degree(reduced_form)
		print_reduced_form(display_form)
		print_degree(degree)
		solve_polynomial(reduced_form, degree)
	
		return 0

	except ValueError as e:
		print(f"Error: {e}")
		return 1

# TODO: use raise systemExit
if __name__ == "__main__":
	sys.exit(main())

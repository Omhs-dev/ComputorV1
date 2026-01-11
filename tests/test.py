import os, sys, unittest

from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.parsing import parse_input
from src.polynomial import reduce_equation, format_reduced_form, get_degree, solve_polynomial

# command: python3 -m unittest -v
def run_flow(equation: str):
	l_dict, r_dict = parse_input(equation)
	reduced = reduce_equation(l_dict, r_dict)
	display = format_reduced_form(reduced)
	degree = get_degree(reduced)
	return l_dict, r_dict, reduced, display, degree

class TestMainFlow(unittest.TestCase):
	def test_flow_degree_2(self):
		cases = [
			# delta > 0 -> two distinct real solutions (1 and 2)
			("1 * X^2 - 3 * X^1 + 2 * X^0 = 0 * X^0", "positive", ["1", "2"]),
			# delta = 0 -> one real solution (2)
			("1 * X^2 - 4 * X^1 + 4 * X^0 = 0 * X^0", "zero", ["2"]),
			# delta < 0 -> no real solutions (complex)
			("1 * X^2 + 1 * X^1 + 1 * X^0 = 0 * X^0", "negative", None),
		]

		for eq, expected_sign, expected_roots in cases:
			with self.subTest(eq=eq):
				l, r, reduced, display, degree = run_flow(eq)
				self.assertIsInstance(l, dict)
				self.assertIsInstance(r, dict)
				self.assertIsInstance(reduced, dict)
				self.assertIsInstance(display, str)
				self.assertEqual(degree, 2)
				with patch("sys.stdout", new=StringIO()) as fake_out:
					solve_polynomial(reduced, degree)
					out = fake_out.getvalue()
				self.assertIn(expected_sign, out)
				if expected_roots:
					for root in expected_roots:
						self.assertIn(root, out)
	def test_flow_degree_2(self):
		cases = [
			# two distinct real solutions (1 and 2)
			("1 * X^2 - 3 * X^1 + 2 * X^0 = 0 * X^0", ["1", "2"]),
			# discriminant = 0 -> message and single root 2
			("1 * X^2 - 4 * X^1 + 4 * X^0 = 0 * X^0", ["Discriminant is = 0", "2"]),
			# discriminant < 0 -> complex roots (contain 'i')
			("1 * X^2 + 1 * X^1 + 1 * X^0 = 0 * X^0", ["i"]),
		]

		for eq, expected_items in cases:
			with self.subTest(eq=eq):
				l, r, reduced, display, degree = run_flow(eq)
				self.assertIsInstance(l, dict)
				self.assertIsInstance(r, dict)
				self.assertIsInstance(reduced, dict)
				self.assertIsInstance(display, str)
				self.assertEqual(degree, 2)
				# Capture solver output and check expected markers/roots
				with patch("sys.stdout", new=StringIO()) as fake_out:
					solve_polynomial(reduced, degree)
					out = fake_out.getvalue()
				for item in expected_items:
					self.assertIn(item, out)

	def test_flow_degree_1(self):
		eq = "-1 * X^1 + 2 * X^0 = 0 * X^0"
		_, _, _, _, degree = run_flow(eq)
		self.assertEqual(degree, 1)

	def test_flow_degree_0(self):
		cases = [
			("42 * X^0 = 42 * X^0", "All real numbers are solutions"),
			("8 * X^0 = 8 * X^0", "All real numbers are solutions"),
			("42 * X^0 = 42 * X^0", "All real numbers are solutions"),
			("5 * X^0 = 3 * X^0", "No solution"),
			("0 * X^0 = 1 * X^0", "No solution"),
		]

		for eq, expected_msg in cases:
			with self.subTest(eq=eq):
				_, _, reduced, _, degree = run_flow(eq)
				self.assertEqual(degree, 0)
				with patch("sys.stdout", new=StringIO()) as fake_out:
					solve_polynomial(reduced, degree)
					out = fake_out.getvalue()
				self.assertIn(expected_msg, out)

	# ...existing code...
	def test_cubic_degree(self):
		eq = "-1 * X^3 + 0.5 * X^2 - 4 * X^0 = +2 * X^1"
		_, _, reduced, _, degree = run_flow(eq)
		self.assertEqual(degree, 3)

		from io import StringIO
		from unittest.mock import patch

		with patch("sys.stdout", new=StringIO()) as fake_out:
			# Should not raise; should print the degree limit message
			solve_polynomial(reduced, degree)
			out = fake_out.getvalue()
		self.assertIn("strictly greater than 2", out)

	def test_leading_signs_on_both_sides(self):
		cases = [
			("+5 * X^2 + 1 * X^0 = +3 * X^2", 2),
			("-5 * X^2 + 1 * X^0 = -3 * X^2", 2),
		]
		for eq, expected_degree in cases:
			with self.subTest(eq=eq):
				l, r, reduced, display, degree = run_flow(eq)
				self.assertIsInstance(l, dict)
				self.assertIsInstance(r, dict)
				self.assertIsInstance(reduced, dict)
				self.assertIsInstance(display, str)
				self.assertNotEqual(display.strip(), "")
				self.assertEqual(degree, expected_degree)
				# Ensure solver runs without raising
				solve_polynomial(reduced, degree)

	def test_flow_zero_coeff_reduction(self):
		eq = "0 * X^2 + 3 * X^1 + 0 * X^0 = 0 * X^0"
		_, _, _, _, degree = run_flow(eq)
		self.assertEqual(degree, 1)

	def test_flow_small_decimal_coeff(self):
		eq = "0.0001 * X^2 = 0 * X^0"
		_, _, _, _, degree = run_flow(eq)
		self.assertEqual(degree, 2)

	def test_invalid_equations_raise(self):
		invalid = [
			"",                                   # Empty
			"General string",                     # Not an equation
			"5 * X^2 + 4 * X^1",                  # Missing '='
			"5 * X^0 = 4 * X^0 = 0 * X^0",        # More than one '='
			"X^2 =",                              # One side empty
			"+3 * X^ = 0",                        # Missing exponent
			"5 * X^0 + 4 * X^1 - 9.3 * X^2",      # Missing right side
			"A * X^0 = 0",                        # Non-numeric coefficient
			"5 * Y^0 = 0 * X^0",                  # Wrong variable
			"5 * X^0 ++ 4 * X^1 = 0",             # Consecutive signs
			"5 * X^0 + - 4 * X^1 = 1 * X^0",      # Consecutive signs with space
			"5 * X ^ 2 = 0 * X^0",                # Bad spacing
			"5*X^0+4*X^1=1*X^0",                  # No spaces at all (invalid per spacing rules)
			"5 * x^2 = 0 * X^0",                  # Lowercase x (if only 'X' allowed)
		]
		for eq in invalid:
			with self.subTest(eq=eq):
				with self.assertRaises(ValueError):
					run_flow(eq)

if __name__ == "__main__":
	unittest.main()

import unittest

from parsing import parse_input
from polynomial import reduce_equation, format_reduced_form, get_degree, solve_polynomial


def run_flow(equation: str):
    # Mimic main() flow without input()
    l_dict, r_dict = parse_input(equation)
    reduced = reduce_equation(l_dict, r_dict)
    display = format_reduced_form(reduced)
    degree = get_degree(reduced)
    return l_dict, r_dict, reduced, display, degree

class TestMainFlow(unittest.TestCase):
    def test_flow_degree_2(self):
        eq = "1 * X^2 - 4 * X^1 + 4 * X^0 = 0 * X^0"
        l, r, reduced, display, degree = run_flow(eq)
        self.assertIsInstance(l, dict)
        self.assertIsInstance(r, dict)
        self.assertIsInstance(reduced, dict)
        self.assertIsInstance(display, str)
        self.assertEqual(degree, 2)
        # Should not raise
        solve_polynomial(reduced, degree)

    def test_flow_degree_1(self):
        eq = "-1 * X^1 + 2 * X^0 = 0 * X^0"
        _, _, _, _, degree = run_flow(eq)
        self.assertEqual(degree, 1)

    def test_flow_degree_0(self):
        eq = "5 * X^0 = 0 * X^0"
        _, _, _, _, degree = run_flow(eq)
        self.assertEqual(degree, 0)

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
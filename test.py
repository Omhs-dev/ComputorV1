import unittest
from parser import term_to_dict

class TestTermToDict(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            term_to_dict(["+5*X^0", "+4*X^1", "-9.3*X^2"]),
            {0: 5.0, 1: 4.0, 2: -9.3}
        )

    def test_duplicates_pruned(self):
        self.assertEqual(
            term_to_dict(["+2*X^1", "+3*X^1", "-5*X^1"]),
            {}
        )

    # def test_invalid_term_raises(self):
    #     with self.assertRaises(ValueError):
    #         term_to_dict(["+2*X^1", "bad"])

if __name__ == "__main__":
    unittest.main()

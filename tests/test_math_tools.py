import unittest
from my_dir.math_tools import is_number_prime, is_number_positive


class TestIsNumberPrime(unittest.TestCase):
    # 7 jest liczba pierwsza
    def test_is_number_prime_standard(self):
        self.assertTrue(is_number_prime(7))

    # 8 nie jest liczba pierwsza
    def test_is_number_prime_not_prime(self):
        self.assertFalse(is_number_prime(8))

    # 1 nie jest liczba pierwsza
    def test_is_number_prime_edge_case_1(self):
        self.assertFalse(is_number_prime(1))

    # 2 jest liczba pierwsza
    def test_is_number_prime_edge_case_2(self):
        self.assertTrue(is_number_prime(2))

    # duza liczba pierwsza
    def test_is_number_prime_large_prime(self):
        self.assertTrue(is_number_prime(104729))

    # duzy liczba nie pierwsdza
    def test_is_number_prime_large_non_prime(self):
        self.assertFalse(is_number_prime(1000000))


class TestIsNumberPositive(unittest.TestCase):
    # 5 jest dodatnia liczba
    def test_is_number_positive_standard(self):
        self.assertTrue(is_number_positive(5))

    # 0 nie jest dodatnia liczba
    def test_is_number_positive_zero(self):
        self.assertFalse(is_number_positive(0))

    # ujemna liczba nie jest dodatnia
    def test_is_number_positive_negative(self):
        self.assertFalse(is_number_positive(-3))

    # liczba 1 jest najmniejsza dodatnia liczba (edge case)
    def test_is_number_positive_edge_case(self):
        self.assertTrue(is_number_positive(1))

    # przyklad z duza liczba
    def test_is_number_positive_large_number(self):
        self.assertTrue(is_number_positive(1000000))

    # przyklad z ujemna liczba
    def test_is_number_positive_small_negative(self):
        self.assertFalse(is_number_positive(-0.0001))


if __name__ == "__main__":
    unittest.main()

import unittest
from my_dir.data_utils import convert_to_uppercase, convert_to_lowercase, is_on_list


class TestConvertToUpperCase(unittest.TestCase):
    def test_convert_to_uppercase_standard(self):
        self.assertEqual(convert_to_uppercase("siema"), "SIEMA")

    def test_convert_to_uppercase_empty(self):
        self.assertEqual(convert_to_uppercase(""), "")

    def test_convert_to_uppercase_mixed(self):
        self.assertEqual(convert_to_uppercase("SiEmA"), "SIEMA")

    def test_convert_to_uppercase_numbers(self):
        self.assertEqual(convert_to_uppercase("siema33"), "SIEMA33")

    def test_convert_to_uppercase_special_chars(self):
        self.assertEqual(convert_to_uppercase("sie#ma!@#"), "SIE#MA!@#")


class TestConvertToLowerCase(unittest.TestCase):
    def test_convert_to_lowercase_standard(self):
        self.assertEqual(convert_to_lowercase("SIEMA"), "siema")

    def test_convert_to_lowercase_empty(self):
        self.assertEqual(convert_to_lowercase(""), "")

    def test_convert_to_lowercase_mixed(self):
        self.assertEqual(convert_to_lowercase("SiEmA"), "siema")

    def test_convert_to_lowercase_numbers(self):
        self.assertEqual(convert_to_lowercase("SIEMA33"), "siema33")

    def test_convert_to_lowercase_special_chars(self):
        self.assertEqual(convert_to_lowercase("SIE#MA!@#"), "sie#ma!@#")


class TestIsOnList(unittest.TestCase):
    def test_is_on_list_standard(self):
        self.assertTrue(is_on_list([1, 2, 3], 2))

    def test_is_on_list_not_present(self):
        self.assertFalse(is_on_list([1, 2, 3], 4))

    def test_is_on_list_empty_list(self):
        self.assertFalse(is_on_list([], 1))

    def test_is_on_list_empty_string(self):
        self.assertTrue(is_on_list([""], ""))

    def test_is_on_list_mixed_types_present(self):
        self.assertTrue(is_on_list([1, "test", 3.5], "test"))

    def test_is_on_list_large_list_present(self):
        self.assertTrue(is_on_list(list(range(1000000)), 999999))

    def test_is_on_list_large_list_not_present(self):
        self.assertFalse(is_on_list(list(range(1000000)), 1000001))


if __name__ == "__main__":
    unittest.main()

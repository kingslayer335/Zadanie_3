import unittest
from my_dir.text_processing import count_words, count_characters, reverse_text


class TestCountWords(unittest.TestCase):
    # testy sprawdzajace poprawnosc liczenia wyrazow w tym te ze specjalnymi znakami, i bardzo dlugim stringiem
    def test_count_words_standard(self):
        self.assertEqual(count_words("Siema siema"), 2)

    def test_count_words_single_word(self):
        self.assertEqual(count_words("Siema"), 1)

    def test_count_words_with_special_chars(self):
        self.assertEqual(count_words("Siema! Si#ma"), 2)

    def test_count_words_large_input(self):
        self.assertEqual(count_words(" ".join(["siema"] * 1000)), 1000)


class TestCountCharacters(unittest.TestCase):
    # testy sprawdzajace poprawnosc liczenia znakow w stringu, w tym te ze specjalnymi znakami, dlugim stringiem, ze spacja i pusty string
    def test_count_characters_standard(self):
        self.assertEqual(count_characters("Siema"), 5)

    def test_count_characters_empty(self):
        self.assertEqual(count_characters(""), 0)

    def test_count_characters_with_spaces(self):
        self.assertEqual(count_characters("Siema 1"), 7)

    def test_count_characters_special_chars(self):
        self.assertEqual(count_characters("12345!@#$%"), 10)

    def test_count_characters_large_input(self):
        self.assertEqual(count_characters("a" * 10000), 10000)


class TestReverseText(unittest.TestCase):
    # testy sprawdzajace poprawnosc odwrotnosci stringow (zwykly, pusty string, string ze spacja, i dlugi string)
    def test_reverse_text_standard(self):
        self.assertEqual(reverse_text("Siema"), "ameiS")

    def test_reverse_text_empty(self):
        self.assertEqual(reverse_text(""), "")

    def test_reverse_text_with_spaces(self):
        self.assertEqual(reverse_text("Siema Siema"), "ameiS ameiS")

    def test_reverse_text_large_input(self):
        self.assertEqual(reverse_text("a" * 10000), "a" * 10000)


if __name__ == "__main__":
    unittest.main()

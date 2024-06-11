import unittest
import strings

class TestPermutations(unittest.TestCase):

    def test_differnt_length(self):
        self.assertFalse(strings.is_strings_permutations("abs", "abbc"))

    def test_same_length(self):
        self.assertTrue(strings.is_strings_permutations("abs", "abs"))

    def test_permutation_is_true(self):
        self.assertTrue(strings.is_strings_permutations("aaabbbsss", "ssaaabsbb"))

    def test_permutation_is_false(self):
        self.assertFalse(strings.is_strings_permutations("aaabbbssb", "ssaaabsbb"))


if __name__ == "__main__":
    unittest.main()

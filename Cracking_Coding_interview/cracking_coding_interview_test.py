import unittest
import cracking_coding_interview as cci

class TestExersizes(unittest.TestCase):

    # Exercise 1.3
    def test_1_3(self):
        self.assertEqual(cci.replace_spaces("Mr John Smith"), "Mr%20John%20Smith")

    def test_1_3_with_lenght(self):
        self.assertEqual(cci.replace_spaces("Mr John Smith    ", 13), "Mr%20John%20Smith")

    # Exercise 1.4
    def test_1_4_odd_length_true(self):
        self.assertTrue(cci.is_string_palindrome_permutation("11223"))

    def test_1_4_odd_length_false(self):
        self.assertFalse(cci.is_string_palindrome_permutation("1112223"))

    def test_1_4_even_length_false(self):
        self.assertFalse(cci.is_string_palindrome_permutation("112  234"))

    def test_1_4_even_length_true(self):
        self.assertTrue(cci.is_string_palindrome_permutation("1232 13"))

    # Exercise 1.7
    def test_1_7(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

        r_matrix = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ]
        self.assertEqual(cci.rotate_matrix(matrix), r_matrix)

    def test_1_8(self):
        orig_matrix = [
            [3, 6, 0, 3, 6],
            [3, 9, 4, 7, 8],
            [3, 7, 9, 0, 9],
            [9, 8, 2, 9, 2],
            [1, 8, 5, 0, 9],
        ]

        res_matrix = [
            [0, 0, 0, 0, 0],
            [3, 9, 0, 0, 8],
            [0, 0, 0, 0, 0],
            [9, 8, 0, 0, 2],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(cci.zero_matrix(orig_matrix), res_matrix)




if __name__ == "__main__":
    unittest.main()
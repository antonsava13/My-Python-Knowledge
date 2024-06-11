import unittest
import quick_sort

class TestQuickSort(unittest.TestCase):

    def setUp(self):
        # get a quicksort funtion
        self.qs = quick_sort.QuickSort().quick_sort
        # unsorted_list = [1, 9, 3, 7, 8, 6, 2, 4, 5]
        # unsorted_list_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        # unsorted_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_are_running(self):
        print("\nTests are running")

    def test_should_return_nothing_for_empty_list(self):
        self.assertEqual(self.qs(["1", "2", "3"], 0, 0), None)

    def test_should_return_list_with_one_member(self):
        list_to_sort = ["3"]
        result = self.qs(list_to_sort)
        self.assertEqual(result, list_to_sort)

    def test_should_sort_list_32(self):
        list_to_sort = ["3", "2"]
        result = self.qs(list_to_sort)
        self.assertEqual(result, ["2", "3"])

    def test_should_sort_list_23(self):
        list_to_sort = ["2", "3"]
        result = self.qs(list_to_sort)
        self.assertEqual(result, ["2", "3"])

    def test_should_sort_list_132(self):
        list_to_sort = ["1", "3", "2"]
        result = self.qs(list_to_sort)
        self.assertEqual(result, ["1", "2", "3"])

    def test_should_sort_123456(self):
        self.assertEqual(self.qs(["1", "2", "3", "4", "5", "6"]), ["1", "2", "3", "4", "5", "6"])

    def test_should_sort_126453(self):
        self.assertEqual(self.qs(["1", "2", "6", "4", "5", "3"]), ["1", "2", "3", "4", "5", "6"])

    def test_should_sort_98764235(self):
        self.assertEqual(self.qs(["9", "8", "7", "6", "4", "2", "3", "5"]), ['2', '3', '4', '5', '6', '7', '8', '9'])

    def test_should_sort_321456(self):
        self.assertEqual(self.qs(["3", "2", "1", "4", "5", "6"]), ["1", "2", "3", "4", "5", "6"])

    def test_should_sort_87912(self):
        self.assertEqual(self.qs(["8", "7", "9", "1", "2"]), ['1', '2', '7', '8', '9'])

    def test_should_sort_987654321(self):
        self.assertEqual(self.qs(["9", "8", "7", "6", "5", "4", "3", "2", "1"]), ["1", "2", "3", "4", "5", "6", "7", "8", "9"])


if __name__ == '__main__':
    unittest.main()
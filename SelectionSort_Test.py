import unittest
from SelectionSort import Selection_Sort


class SelectionSortAlgorithmTest(unittest.TestCase):
    def test_BubbleSort(self):
        self.assertEqual(Selection_Sort([117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]),
                                        [1, 3, 5, 6, 8, 16, 22, 28, 29, 32, 34, 41, 42, 49, 50, 51, 63, 64, 69, 74, 77, 81, 83, 88, 90, 117])
        self.assertEqual(Selection_Sort([7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]),
                                        [0, 1, 1, 1, 4, 4, 4, 4, 5, 5, 7, 7, 7, 7, 7, 7, 9, 9])
        self.assertEqual(Selection_Sort([-7, -7, -7, 7, 7, -1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]),
                                        [-7, -7, -7, -1, 0, 1, 1, 4, 4, 4, 4, 5, 5, 7, 7, 7, 9, 9])


if __name__ == "__main__":
    unittest.main()
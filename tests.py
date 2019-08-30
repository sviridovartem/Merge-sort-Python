import merge_sort as my_sort
import unittest


class TestSortMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_correct_sorting(self):
        self.assertEqual(my_sort.merge_sort([15, 13, 11, 16, 18, 69, 46, 22, 11, 10, 8, 5, 8]),
                         sorted([15, 13, 11, 16, 18, 69, 46, 22, 11, 10, 8, 5, 8]))

    def test_empty_list(self):
        self.assertEqual(my_sort.merge_sort([]), [])

    def test_correct_sorting_with_negative_elements_list(self):
        self.assertEqual(my_sort.merge_sort([-15, -13, -11, -16, -18, -69, -46, -22, -11, -10, -8, -5, -8]),
                         sorted([-15, -13, -11, -16, -18, -69, -46, -22, -11, -10, -8, -5, -8]))

    def test_correct_sorting_with_mixed_negative_and_positive_elements_list(self):
        self.assertEqual(my_sort.merge_sort([-15, -13, -11, 16, -18, 69, -46, 22, -11, 0, -8, -5, -8]),
                         sorted([-15, -13, -11, 16, -18, 69, -46, 22, -11, 0, -8, -5, -8]))

    def test_mixed_types_inside_list(self):
        self.assertRaises(ValueError, my_sort.merge_sort, [4, "f", "t", "p", "g", "f", "e", "p"])

    def test_mixed_types_inside_list1(self):
        self.assertRaises(TypeError, my_sort.merge_sort, [4, "f", "t", "p", "g", "f", "e", "p"],
                          [4, "f", "t", "p", "g", "f", "e", "p"])


def main():
    test_list = [[{1, 2, 3, 4, 4, 5}, {13, 2, 4, 5, 6, }]]
    print(my_sort.merge_sort(test_list))


if __name__ == '__main__':
    main()
    unittest.main()

import unittest
import random

from helper.list import List
from helper.search_functions import binary_search, search, SearchStrategy


def create_array(param):
    lst = random.sample(range(1, 100000), param)
    return sorted(lst)


class TestSearchFunctions(unittest.TestCase):
    def setUp(self):
        self.array_size = 100
        self.test_list = List(create_array(self.array_size), "randomWord")

    def test_binary_search(self):
        expected_index = random.randint(0, self.array_size)
        key = self.test_list.lst[expected_index]

        returned_index = search(self.test_list, self.array_size, 0, key, SearchStrategy.BINARY)
        self.assertEqual(returned_index, expected_index)

        expected_index = self.array_size - 1
        key = self.test_list.lst[expected_index]

        returned_index = search(self.test_list, self.array_size, 0, key, SearchStrategy.BINARY)
        self.assertEqual(returned_index, expected_index)

    def test_linear_search(self):
        expected_index = random.randint(0, self.array_size)
        key = self.test_list.lst[expected_index]

        returned_index = search(self.test_list, self.array_size, 0, key, SearchStrategy.LINEAR)

        self.assertEqual(returned_index, expected_index)


if __name__ == '__main__':
    unittest.main()

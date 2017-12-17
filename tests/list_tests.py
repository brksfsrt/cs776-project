import random
import unittest

from helper.list import List


def create_array(param):
    lst = random.sample(range(1, 100000), param)
    return sorted(lst)


class TestListFunctions(unittest.TestCase):
    def setUp(self):
        self.array_size = 100
        self.test_list = List(create_array(self.array_size), "randomWord")

    def test_f_search(self):
        expected_index = random.randint(0, self.array_size - 5)
        key = self.test_list.lst[expected_index]

        returned_index = self.test_list.f_search(key, 4)
        self.assertEqual(returned_index, expected_index)

        expected_index += 5
        key = self.test_list.lst[expected_index]

        returned_index = self.test_list.f_search(key, 4)
        self.assertEqual(returned_index, expected_index)

        unreachable_index = expected_index - 5
        key = self.test_list.lst[unreachable_index]

        returned_index = self.test_list.f_search(key, 4)
        self.assertEqual(returned_index, -1)

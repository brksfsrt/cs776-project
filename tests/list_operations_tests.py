import random
import unittest

from helper.list import List
from helper.list_operations import binary_intersect


def create_array(param):
    lst = random.sample(range(1, 100000), param)
    return sorted(lst)


class TestListFunctions(unittest.TestCase):
    def setUp(self):
        array_size = 100

        self.common_arr = create_array(array_size-1) + [100000]
        self.test_lst1 = List(sorted(set(create_array(array_size * 10) + self.common_arr)), "word1")
        self.test_lst2 = List(sorted(set(create_array(array_size) + self.common_arr)), "word2")

    def test_binary_intersect(self):
        ret_list = binary_intersect(self.test_lst1, self.test_lst2)
        self.assertTrue(len(ret_list.lst) >= len(self.common_arr))
        self.assertTrue(len(set(self.common_arr) - set(ret_list.lst)) == 0)


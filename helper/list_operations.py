import collections

from helper.list import List
from helper.search_functions import search


def equal(list_obj1, list_obj2):
    return collections.Counter(list_obj1.lst) == collections.Counter(list_obj2.lst)


# TODO: implement intersect method
def intersect(list_obj1, list_obj2):
    pass


def diff(list_obj1, list_obj2):
    diff_list = list(list_obj1.lst - list_obj2.lst)
    return List(diff_list)


def split(list_obj, x):
    index = search(list_obj, list_obj.size - list_obj.current_position, x)

    if index == -1:
        raise ValueError("Element could not found.")

    list1, list2 = list_obj.lst[:index], list_obj.lst[index:]
    return List(list1), List(list2)



import collections

from helper.list import List
from helper.search_functions import search


def equal(list_obj1, list_obj2):
    return collections.Counter(list_obj1.lst) == collections.Counter(list_obj2.lst)


def binary_intersect(list_obj1, list_obj2):
    ret_list = []
    small_list = list_obj2 if len(list_obj1.lst) > len(list_obj2.lst) else list_obj1
    big_list = list_obj1 if len(list_obj1.lst) > len(list_obj2.lst) else list_obj2

    x = small_list.succ()

    while x != -1:
        y = big_list.f_search(x, int(len(big_list.lst) / len(small_list.lst)))
        if x == big_list.lst[y]:
            ret_list.append(x)
        x = small_list.succ()

    return List(ret_list, small_list.word + " and " + big_list.word)


def diff(list_obj1, list_obj2):
    diff_list = list(list_obj1.lst - list_obj2.lst)
    return List(diff_list)


def split(list_obj, x):
    index = search(list_obj, list_obj.size - list_obj.current_position, x)

    if index == -1:
        raise ValueError("Element could not found.")

    list1, list2 = list_obj.lst[:index], list_obj.lst[index:]
    return List(list1), List(list2)

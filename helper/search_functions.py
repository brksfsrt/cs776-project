from helper.list import List

from enum import Enum


class SearchStrategy(Enum):
    LINEAR = 1
    BINARY = 2


def binary_search_helper(list_obj, end, key, start=0):
    if start > end:
        return -1

    middle = end - start / 2

    if list_obj.lst[middle] == key:
        return middle
    elif list_obj.lst[middle] > key:
        binary_search_helper(list_obj, middle - 1, key, start)
    else:
        binary_search_helper(list_obj, end, key, middle + 1)


def binary_search(list_obj, size, key):
    binary_search_helper(list_obj.lst, size, key)


def linear_search(list_obj, size, key):
    for index, item in enumerate(list_obj.lst):
        if item == key:
            return index
        elif item > key:
            return -1

    return -1


def search(list_obj, size, key, strategy=SearchStrategy.BINARY):
    """Return the index relative to current position in list object by using strategy given"""
    if strategy == SearchStrategy.LINEAR:
        return linear_search(list_obj, size, key)
    elif strategy == SearchStrategy.BINARY:
        return binary_search(list_obj, size, key)

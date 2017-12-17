from enum import Enum


class SearchStrategy(Enum):
    LINEAR = 1
    BINARY = 2


def binary_search_helper(list_obj, end, start, key):
    if start > end:
        return -1

    middle = int((end + start) / 2)

    if list_obj[middle] == key:
        return middle
    elif list_obj[middle] > key:
        return binary_search_helper(list_obj, middle - 1, start, key)
    else:
        return binary_search_helper(list_obj, end, middle + 1, key)


def binary_search(list_obj, end, start, key):
    return binary_search_helper(list_obj.lst, end, start, key)


def linear_search(list_obj, end, start, key):
    sliced_list = list_obj.lst[start:end]
    for index, item in enumerate(sliced_list):
        if item == key:
            return index + start
        elif item > key:
            return -1

    return -1


def search(list_obj, end, start, key, strategy=SearchStrategy.BINARY):
    """Return the index relative to current position in list object by using strategy given"""
    if strategy == SearchStrategy.LINEAR:
        return linear_search(list_obj, end, start, key)
    elif strategy == SearchStrategy.BINARY:
        return binary_search(list_obj, end, start, key)

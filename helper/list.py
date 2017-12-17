from helper.search_functions import search, SearchStrategy


class List:
    def __init__(self, lst, word):
        self.lst = lst
        self.current_position = 0
        self.size = len(lst)
        self.word = word

    def succ(self):
        self.current_position += 1
        self.size -= 1
        return self.lst[self.current_position - 1] if self.current_position <= len(self.lst) else -1

    def pred(self):
        if self.current_position != 0 and self.size != 0:
            self.size += 1
            self.current_position -= 1

    def range_list(self, x, y):
        start = search(self, self.size - self.current_position, x)
        end = search(self, self.size - self.current_position, y)

        if start == -1 or end == -1:
            raise ValueError("Element could not found.")

        self.lst = self.lst[start:end]
        self.current_position = 0
        self.size = end - start

    def select(self, r):
        if r > self.size:
            raise ValueError("List size is smaller than given index")

        self.current_position += r
        self.size -= r

    def f_search(self, key, golomb_parameter):
        init_current_position = self.current_position
        position = self.current_position + golomb_parameter
        while position < len(self.lst) and self.lst[position] < key:
            self.current_position = position
            position = self.current_position + golomb_parameter

        if position > len(self.lst):
            position = len(self.lst)

        offset = search(self, position, self.current_position, key, SearchStrategy.BINARY)

        if offset == position:
            self.current_position = position
            self.size -= self.current_position - init_current_position
        else:
            self.current_position = offset
            self.size -= self.current_position - init_current_position

        if self.current_position > len(self.lst):
            return -1
        else:
            return self.current_position

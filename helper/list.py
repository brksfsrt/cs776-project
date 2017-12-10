from helper.search_functions import search


class List:
    def __init__(self, lst, word):
        self.lst = lst
        self.current_position = 0
        self.size = lst.size()
        self.word = word

    def succ(self):
        self.current_position += 1
        self.size -= 1

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

# TODO: implement f_search method
    def f_search(self):
        pass

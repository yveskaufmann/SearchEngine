from collections import UserList
import os

class Hit:
    def __init__(self, page_id, score):
        self.page_id = page_id
        self.score = score

    def __str__(self):
        return self.page_id + ':' + (' ' * 4) + '{:.6f}'.format(self.score)

class Hits(UserList):
    def __init__(self, query):
        super().__init__()
        self.query = query

    def sort(self, key=None, reverse=True):
        if key is None:
            key = self.__sort_key
        self.data.sort(key=key, reverse=reverse)

    def __sort_key(self, hit):
        return hit.score

    def __str__(self):
        """ Create the string representation of all pages """
        output = []

        output.append(str(self.query))
        hit_list = (str(hit) for hit in self)
        output.append(os.linesep.join(hit_list))

        return os.linesep.join(output)


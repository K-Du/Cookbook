# As a function

from collections import defaultdict
tree = lambda: defaultdict(tree)


# As a class

class Tree(dict):
    def __missing__(self, key):
    value = self[key] = type(self)()
        return value

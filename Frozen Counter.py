# Gives the Counter class a hash attribute

from collections import Counter

class FrozenCounter(Counter):
    def __hash__(self):
        return hash(frozenset(self.items()))

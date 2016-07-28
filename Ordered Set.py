# Removes duplicates from a list while preserving order

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]



# Using OrderedDict
from collections import OrderedDict
list(OrderedDict.fromkeys(seq))  

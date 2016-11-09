from bisect import bisect_left 

def binary_search(a, x, lo=0, hi=None):   
    hi = hi if hi is not None else len(a) 
    pos = bisect_left(a,x,lo,hi)      
    return (pos if pos != hi and a[pos] == x else -1)
    
# No imports

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   
                break        
            lower = x
        elif target < val:
            upper = x

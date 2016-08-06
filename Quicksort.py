# Quicksort implementation

def quicksort(A, lo=0, hi=len(A)-1):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

# Lomuto partition

def partition(array, start, end):
    pivot = start  
    for i in range(start, end): 
        if array[i] <= array[end]:  
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1
    array[end], array[pivot] = array[pivot], array[end]  # swap pivot value and value at pivot position
    return pivot

# Hoare partition

def partition(array, start, end):
    i, j = start, end - 1
    while True:
        while array[i] <= array[end] and i < j:
            i += 1
        while array[j] >= array[end] and i < j:
            j -= 1
        if i == j:
            if array[i] <= array[end]:
                i += 1
            array[i], array[end] = array[end], array[i]
            return i
        else:
            array[i], array[j] = array[j], array[i]
        

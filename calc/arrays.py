import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

def fill_full(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    if seed is not None:
        random.seed(seed)
    data = [random.randint(low, high) for n in range(count)]
    return data

def binary_search(data, target):
    left = 0
    right = len(data) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == target:
            return middle
        if data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
            
    return None
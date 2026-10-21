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
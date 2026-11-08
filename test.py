from calc.sorting import *
from mathtool import *
import time


data = read_mas("example.txt")


start = time.perf_counter()
counting(data.copy())
elapsed_time = time.perf_counter() - start
print(elapsed_time)

start = time.perf_counter()
counting(data.copy(), min = -100, max= 100)
elapsed_time = time.perf_counter() - start
print(elapsed_time)



from calc.arrays import (MIN_VALUE, MAX_VALUE)

def ne_po_poradku(a, b , descending):
    if descending:
        return a < b
    return a > b

def bubble(data, descending=False):
    n = len(data)
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if ne_po_poradku(data[j], data[j + 1], descending):
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True
        if not swap:
            break
    return data





METHODS = {
    "bubble": bubble
    }

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

def selection(data, descending=False):
    n = len(data)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if ne_po_poradku(data[best], data[j], descending):
                best = j
        data[i], data[best] = data[best], data[i]
    return data

def insertion(data, descending=False):
    n = len(data)
    for i in range(1, n):
        current = data[i]
        j = i
        while j > 0 and ne_po_poradku(data[j - 1], current, descending):
            data[j] = data[j - 1]
            j -= 1
        data[j] = current
    return data

def counting(data, descending=False):
    counters_size = MAX_VALUE - MIN_VALUE + 1
    counters = [0] * counters_size
    
    for value in data:
        counters[value - MIN_VALUE] += 1
        
    k = 0
    num = list(range(counters_size))

    if descending:
        num.reverse()

    for index in num:
        for n in range(counters[index]):
            data[k] = index + MIN_VALUE
            k += 1
    return data



METHODS = {
    "bubble": bubble,
    "selection": selection,
    "insertion": insertion,
    "counting": counting
    }

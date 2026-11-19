from calc.arrays import (MIN_VALUE, MAX_VALUE)

def ne_po_poradku(a, b , descending):
    if descending:
        return a < b
    return a > b

def ranshe(a, b , descending):
    if descending:
        return a > b
    return a < b

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

def counting(data, descending=False, min = MIN_VALUE, max = MAX_VALUE):
    counters_size = max - min + 1
    counters = [0] * counters_size
    
    for value in data:
        counters[value - min] += 1
        
    k = 0
    num = list(range(counters_size))

    if descending:
        num.reverse()

    for index in num:
        for n in range(counters[index]):
            data[k] = index + min
            k += 1
    return data


def quick(data, descending=False):
    uporadochit(data, 0, len(data) - 1, descending)


def uporadochit(data, left, right, descending):
    if left >= right:
        return
    opora = data[(left+right) // 2]
    i = left
    j = right

    while i <= j:
        while ranshe(data[i], opora, descending): 
            i += 1
        while ranshe(opora, data[j], descending): 
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
    uporadochit(data, left, j, descending)
    uporadochit(data, i, right, descending)

def merge(data, descending=False):
    uporadochit_fusion(data, 0, len(data) - 1, descending)

def uporadochit_fusion(data, left, right, descending):
    if left >= right:
        return
    mid = (left+right) // 2
    uporadochit_fusion(data,left,mid,descending)
    uporadochit_fusion(data,mid+1,right,descending)
    slit(data,left,mid,right,descending)

def slit(data,left,mid,right,descending):
    result = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if ranshe(data[j], data[i], descending):
            result.append(data[j])
            j += 1
        else:
            result.append(data[i])
            i += 1
    result.extend(data[i:mid + 1])
    result.extend(data[j:right + 1])
    
    data[left:right + 1] = result

def proseat(data, i, size, descending):
    while True:
        choose = i
        for c in [2*i+1,2*i+2]:
            if c < size:
                if ranshe(data[choose], data[c], descending):
                    choose = c
        if choose == i:
            return
        data[i], data[choose] = data[choose], data[i]
        i = choose


def heap(data, descending=False):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        proseat(data, i, n, descending)
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        proseat(data, 0, end, descending) 



METHODS = {
    "bubble": bubble,
    "selection": selection,
    "insertion": insertion,
    "counting": counting,
    "quick": quick,
    "merge": merge, 
    "heap": heap
    }

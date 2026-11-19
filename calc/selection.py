import random

def breaking(data, left, right, rng):
    q = rng.randint(left, right)
    data[q], data[right] = data[right], data[q]
    opora = data[right]
    i = left
    for j in range(left,right):
        if data[j] <= opora:
            data[i], data[j] = data[j], data[i] 
            i += 1
    data[i], data[right] = data[right], data[i]
    return i

def statistika(data, k, seed = False):
    if isinstance(k, bool) or not isinstance(k, int):
        raise ValueError("Порядковый номер k должен быть целым числом.")
    if not data or k < 1 or k > len(data):
        raise ValueError(f"Номер статистики k должен быть от 1 до {len(data)}.")

    rng = random.Random(seed)
    target = k - 1
    left = 0
    right = len(data) - 1

    while left < right:
        p = breaking(data, left, right, rng)
        if target == p:
            return data[p]
        if target < p:
            right = p - 1
        else:
            left = p + 1
    return data[left]
    
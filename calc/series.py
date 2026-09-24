import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000

def sign(n):
    if n % 2:
        return 1
    else:
        return -1

def s_sqplus(n):
    return sign(n) / (n ** 2 + 1)

def s_third(n):
    return sign(n) / (3 * n)


FORMULAS = {
    "sqplus": (s_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (s_third, "S = 1/3 - 1/6 + 1/9 - 1/12 + ...")
}

def summa_by_count(term, count):
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result

def summa_by_eps(term, eps):
    result = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("Точность не достигнута")
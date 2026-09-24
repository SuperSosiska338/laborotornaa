import math

MAX_NUM = 20
MAX_ABSNUM = 10000


def summa(values):
    result = 0
    for value in values:
        result += value
    return result

def srednee(values):
    return summa(values)/len(values)

def summa_kvadratov(values):
    result = 0
    for value in values:
        result += value**2
    return result

def srednee_kvadrat(values):
    return math.sqrt(summa_kvadratov(values) / len(values))

def minimum(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result

def maximum(values):
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result

def kol_polojitelnih(values):
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result

def kol_otricatelnih(values):
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result

def summa_kvadratov_otkloneniy(values):
    sredne = srednee(values)
    result = 0
    for value in values:
        result += (value - sredne)**2
    return result

def dispersia(values):
    return summa_kvadratov_otkloneniy(values)/len(values)

def SKO(values):
    return math.sqrt(dispersia(values))

def standart_otlonenie(values):
    if len(values) < 2:
        return None
    return math.sqrt(summa_kvadratov_otkloneniy(values)/(len(values) - 1))

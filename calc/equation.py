MAX_VALUE = 10000

def solve(a, b, c):

    if a == 0:
           if b != 0:
                  x = -c / b
                  return "Линейное", None, [x]
           else:
                  raise ValueError("ОШИБКА: это не уравнение, неизвестное отсутствует")
    else:
            D = (b**2) - (4*a*c)
    if D > 0:
                   x1 = (-b + D**(1/2))/(2*a)
                   x2 = (-b - D**(1/2))/(2*a)
                   return "Квадратное", D, [x1, x2]
    elif D == 0:
                   x = -b / (2*a)
                   return "Квадратное", D, [x]
    else:
                   return "Квадратное", D, []

def ogr():
        try:
                a = int(a1)
                b = int(b1)
                c = int(c1)
        except ValueError:
                   raise ValueError("ОШИБКА: коэффициент не является целым числом")
                   sys.exit(1)
        
        if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
                    raise ValueError("ОШИБКА: значение вне допустимого диапазона")
                    sys.exit(1)

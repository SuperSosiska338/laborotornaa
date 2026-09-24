import sys

MAX_VALUE = 10000

def solve(a, b, c):

    if a == 0:
            x = -c / b
            return "Линейное", None, [x]
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

def ogr(a, b, c):
        try:
                a = int(a)
                b = int(b)
                c = int(c)
        except ValueError:
                   raise ValueError("Коэффициент не является целым числом")

        if a == 0 & b == 0:
                    raise ValueError("Это не уравнение, неизвестное отсутствует")


        check_max({"A": a, "B": b, "C": c})

def check_max(coefficients):
   for name, value in coefficients.items():
      if  abs(value) > MAX_VALUE:
        raise ValueError(f"Коэффициент {name} вне допустимого диапазона")
      

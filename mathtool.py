import sys
import math
import cli
from calc import equation, stats, integration, series


def print_solve(args):

    count = sum(x is not None for x in [args.a, args.b, args.c])
    if count == 0:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:

            raise ValueError("Введённый коэффициент не является целым числом")
    else:
        a, b, c = args.a, args.b, args.c

    equation.ogr(a, b, c)
    kind, d, roots = equation.solve(a, b, c)



    if kind == "Линейное":
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")
    else:
        print("Уравнение квадратное")
        print(f"Дискриминант: {d}")
        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print("Действительных корней нет")
    return 0

def print_stats(args):

    if args.input:
        with open(args.input, "r", encoding="utf-8-sig") as n:
           num = n.read()
    else:
        num = sys.stdin.read()

    numders = num.split()
    if not numders:
        raise ValueError("Список пуст")

    values = []
    for number in numders:
        try:
            val = float(number)
        except ValueError:
            raise ValueError(f"{number} не является числом")

        if not math.isfinite(val):
                       raise ValueError("Значение не является конечным")
           
        if abs(val) > stats.MAX_ABSNUM:
                       raise ValueError("Значение по модулю больше 10000")


        values.append(val)

    if len(values) > stats.MAX_NUM:
                raise ValueError("Чисел больше 20")

    

    number_table = [
        ("Количество", len, "d"),
        ("Сумма", stats.summa, ".3f"),
        ("Срднее арифметическое", stats.srednee, ".3f"),
        ("Сумма квадратов", stats.summa_kvadratov, ".3f"),
        ("Среднее квадратическое", stats.srednee_kvadrat, ".3f"),
        ("Дисперсия", stats.dispersia, ".3f"),
        ("СКО", stats.SKO, ".3f"),
        ("Стандартное отклонение", stats.standart_otlonenie, ".3f"),
        ("Наименьшее", stats.minimum, ".3f"),
        ("Наибольшее", stats.maximum, ".3f"),
        ("Положительных", stats.kol_polojitelnih, "d"),
        ("Отрицательных", stats.kol_otricatelnih, "d"), 
    ]

    for podpis, func, form in number_table:
         result = func(values)
         if result is None:
              print(f"{podpis}: НЕ СУЩЕСТВУЕТ")
         else:
              print(f"{podpis}: {result:{form}}")  
    return 0


def print_series(args):
    term, formula_str = series.FORMULAS[args.func]

    
    if args.terms is not None:
        if not (1 <= args.terms <= series.MAX_TERMS):
            raise ValueError("Количество слагаемых вне диапазона")
        
        print(formula_str)
        res = series.summa_by_count(term, args.terms)
        count = args.terms
    else:
        if (not math.isfinite(args.eps) or not (0 < args.eps <= series.MAX_EPS)):
            raise ValueError("Точность вне диапазона")
        print(formula_str)
        res, count = series.summa_by_eps(term, args.eps)

    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {res:.4f}")
    return 0

def print_integration(args):
     
 func, formula_str, low, high, limit = integration.FUNCTIONS[args.func]

 if not math.isfinite(args.a) or not math.isfinite(args.b):
        raise ValueError("Предел не является конечным числом")
 if args.a >= args.b:
        raise ValueError("начальный предел не меньше конечного")
 if not (1 <= args.steps <= 100000):
        raise ValueError("Количество шагов вне диапазона")
 if limit == False:
        if (args.a <= low or args.a >= high or args.b <= low or args.b >= high):
            raise ValueError("Предел вне промежутка")
 else:
      if (args.a < low or args.a > high or args.b < low or args.b > high):
            raise ValueError("Предел вне промежутка")
 print(formula_str)

 result = integration.integrate(func, args.a, args.b, args.steps)
 print(f"Значение интеграла: {result:.4f}")
 return 0

def main(argv):
   
  parser = cli.commandos()
  args = parser.parse_args(argv)
  

  if args.command is None:
        parser.print_help()
        return 0
  try:
      if args.command == "solve":
          return print_solve(args)
      if args.command == "stats":
          return print_stats(args)
      if args.command == "series":
          return print_series(args)
      if args.command == "integrate":
          return print_integration(args)
  except (ValueError, OSError) as error:
      err = str(error)
      if isinstance(error, OSError):
            err = "Файл не открывается"
      print(f"Ошибка:{err}", file=sys.stderr)
      return 1

      
          

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
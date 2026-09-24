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
    return 1

def print_stats(args):
    MAX_NUM = 20
    MAX_ABSNUM = 10000

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
           
        if abs(val) > MAX_ABSNUM:
                       raise ValueError("Значение по модулю больше 10000")


        values.append(val)

    if len(values) > MAX_NUM:
                raise ValueError("Чисел больше 20")
    

    number_table = [
        ("Количество", len(values), "d"),
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
  except (ValueError, OSError) as error:
      print(f"Ошибка:{error}", file=sys.stderr)

      
          
  



    
                      



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
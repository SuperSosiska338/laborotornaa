import sys
import math
import cli
from calc import equation


def print_solve():
    a, b, c = args.a, args.b, args.c

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

def main(argv):
   
  parser = cli.commandos()

  if not argv:
        parser.print_help()
        return 0




    
                      



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
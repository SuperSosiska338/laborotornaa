import sys
import math
from calc import equation


def main():
    args = len(sys.argv) - 1

    if args == 0 or sys.argv[1] == "--help":
        print(
"mathtool — решение уравнений вида A*x^2 + B*x + C = 0 \nИспользование:\npython mathtool.py -> вывод справки\npython mathtool.py --help -> вывод справки\npython mathtool.py solve -> ввод коэффициентов с клавиатуры\npython mathtool.py solve -a 1 -b -3 -c 2 -> решение с заданными коэффициентами\nКоэффициенты A, B, C — целые числа, по модулю не превышающие 10000."
)
        sys.exit(0)
    elif sys.argv[1] != "solve":
        print("Неизвестная команда", file=sys.stderr)
        sys.exit(1)
    elif sys.argv[1] == "solve" and len(sys.argv) == 2:
        a1 = str(input("Введите A: "))
        b1 = str(input("Введите B: "))
        c1 = str(input("Введите C: "))
    elif len(sys.argv) == 8:
        if sys.argv[2] != "-a" and sys.argv[4] != "-b" and sys.argv[6] != "-c":
            print("Неизвестный параметр", file=sys.stderr)
            sys.exit(1)
        a1=sys.argv[3]
        b1=sys.argv[5]
        c1=sys.argv[7]
    else:
        print("Неверный набор параметров", file=sys.stderr) 
        sys.exit(1) 

    

    kind, d, roots = equation.solve(1, -3, 2)

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



    
                      
    sys.exit(0)


main()
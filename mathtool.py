import sys
import math


def main():
    args = len(sys.argv) - 1

    MAX_VALUE = 10000
    
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

    try:
        a = int(a1)
        b = int(b1)
        c = int(c1)
    except ValueError:
           print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
           sys.exit(1)

    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
            print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
            sys.exit(1)

    if a == 0:
       if b != 0:
              print ("Линейное уравнение")
              x = -c / b
              print (f"x = {x:.3f}")
       else:
              print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
              sys.exit(1)
    else:
        print ("Уравнение квадратное")
        D = (b**2) - (4*a*c)
        print(f"Дискриминант: {D:.3f}")

        if D > 0:
               x1 = (-b + D**(1/2))/(2*a)
               x2 = (-b - D**(1/2))/(2*a)
               print (f"x1 = {x1:.3f}")
               print (f"x2 = {x2:.3f}")
        elif D == 0:
               x = -b / (2*a)
               print (f"x = {x:.3f}")
        else:
               print("Действительных корней нет")
                      
    
    sys.exit(0)
    




              
              







main()
import sys
import math


def main():
    args = len(sys.argv) - 1
    
    if args == 0 or sys.argv[1] == "--help":
        print(
"mathtool — решение уравнений вида A*x^2 + B*x + C = 0 \nИспользование:\npython mathtool.py -> вывод справки\npython mathtool.py --help -> вывод справки\npython mathtool.py solve -> ввод коэффициентов с клавиатуры\npython mathtool.py solve -a 1 -b -3 -c 2 -> решение с заданными коэффициентами\nКоэффициенты A, B, C — целые числа, по модулю не превышающие 10000."
)
        sys.exit(0)
    elif sys.argv[1] != "solve":
        print("Неизвестная команда")
        sys.exit(1)
    elif sys.argv[1] == "solve" and len(sys.argv) == 2:
        a1 = str(input("Введите A: "))
        b1 = str(input("Введите B: "))
        c1 = str(input("Введите C: "))
    elif len(sys.argv) == 8:
        if sys.argv[2] != "-a" and sys.argv[4] != "-b" and sys.argv[6] != "-c":
            print("Неизвестный параметр")
            sys.exit(1)
        a1=sys.argv[3]
        b1=sys.argv[5]
        c1=sys.argv[7]
    else:
        print("Неверный набор параметров") 
        sys.exit(1) 

    try:
        a = int(a1)
        b = int(b1)
        c = int(c1)
    except ValueError:
           print("ОШИБКА: коэффициент не является целым числом")
           sys.exit(1)

    if abs(a) > 10000 or abs(b) > 10000 or abs(c) > 10000:
            print("ОШИБКА: значение вне допустимого диапазона")
            sys.exit(1)

    D = (b**2) - (4*a*c)
    print (f"Дискриминант: {D:.3f}")
            
        
    if D > 0 and a !=0 and b != 0:
                x1 = (-b + D**(1/2))/(2*a)
                x2 = (-b - D**(1/2))/(2*a)
                print (f"x1 = {x1:.3f}")
                print (f"x2 = {x2:.3f}")
                print ("Уравнение квадратное")
    elif D < 0 and a !=0 and b != 0:
                print ("Действительных корней нет")
    elif D == 0 and a !=0 and b != 0:
                x = -b / (2*a)
                print(f"x = {x:.3f}")
                print("Уравнение квадратное")
    elif a == 0 and b !=0:
                x = -c / b
                print (f"x = {x:.3f}") 
                print("Уравнение линейное")  
    elif b == 0 and c > 0:
                print ("Действительных корней нет")
    elif b == 0 and c < 0:
                x = (-c/a)**(1/2)
                print (f"x = {x:.3f}")
                print("Уравнение квадратное")
    elif b==0 and a ==0:
           print("ОШИБКА: это не уравнение, неизвестное отсутствует")       
    
    sys.exit(0)
    



main()
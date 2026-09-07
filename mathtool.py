import sys
import math


def solve():
    args = sys.argv

    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    c = int(input("Введите C: "))
    if abs(a) > 10000 or abs(b) > 10000 or abs(c) > 10000:
        print("ОШИБКА: значение вне допустимого диапазона")
        sys.exit(1)
    

    D = (b**2) - (4*a*c)

    if D > 0 and a !=0 and b != 0:
        x1 = (-b + D**(1/2))/(2*a)
        x2 = (-b - D**(1/2))/(2*a)
        print (x1)
        print (x2)
    elif D < 0 and a !=0 and b != 0:
        print ("no")
    elif D == 0 and a !=0 and b != 0:
        x = -b / (2*a)
        print(x)
    elif a == 0:
        x = -c / b
        print (x)   
    elif b == 0 and c > 0:
        print ("шыш")
    elif b == 0 and c <= 0:
        x = (-c/a)**(1/2)
        print (x)



def main():
    args = len(sys.argv) - 1
    
    if args == 0 or sys.argv[1] == "--help":
        print("pomogite pajalusta")
        sys.exit(0)
    elif sys.argv[1] != "solve":
        print("Неизвестная команда")
        sys.exit(1)
    elif sys.argv[1] == "solve":
        solve()
        sys.exit(0)
    elif sys.argv[7]:
        if sys.argv[2] != "-a" and sys.argv[4] != "-b" and sys.argv[6] != "-c":
            print("Неизвестный параметр")
            sys.exit(1)

    



main()
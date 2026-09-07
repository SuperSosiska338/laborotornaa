import sys
import math

#(Ax**2)+(Bx) + С= 0

def solve():

    args = sys.argv

    a = float(args[2])
    b = float(args[3])
    c = float(args[4])

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


    

    

def print_help():
    print("pomogite pajalusta")

def main():
    args = len(sys.argv) - 1
    
    if args == 0 or sys.argv[1] == "--help":
        print_help()
        sys.exit(0)
    elif sys.argv[1] == "solve":
        solve()


main()
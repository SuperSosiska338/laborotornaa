import sys
import math

#(Ax**2)+(Bx) + С= 0

def solve():
    a = 1
    b = 4
    c = 2

    D = (b**2) - (4*a*c)

    if D > 0:
        x1 = (-b + D**(1/2))/(2*a)
        x2 = (-b - D**(1/2))/(2*a)
        print (x1)
        print (x2)
    elif D < 0:
        print ("no")
    else:
        x = -b / (2*a)
        print(x)

    

    

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
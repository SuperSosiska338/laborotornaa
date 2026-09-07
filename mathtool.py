import sys
import math

def quadratic():

    args = sys.argv

    a = float(args[1])
    b = float(args[2])
    c = float(args[3])

    s1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a) 
    s2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a) 

    print("Ваши решения: ", s1, "и", s2)

def print_help():
    print("pomogite pajalusta")
    
def main():
    args_count = len(sys.argv) - 1
    
    if args_count == 0 or sys.argv[1] == "--help":
        print_help()
        sys.exit(0)
main()
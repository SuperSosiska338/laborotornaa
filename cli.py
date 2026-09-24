import argparse

def commandos():
    parser = argparse.ArgumentParser(prog="mathtool", description=
"mathtool — решение уравнений вида A*x^2 + B*x + C = 0 \nИспользование:\npython mathtool.py -> вывод справки\npython mathtool.py --help -> вывод справки\npython mathtool.py solve -> ввод коэффициентов с клавиатуры\npython mathtool.py solve -a 1 -b -3 -c 2 -> решение с заданными коэффициентами\nКоэффициенты A, B, C — целые числа, по модулю не превышающие 10000.",
 allow_abbrev=False)

    subparsers = parser.add_subparsers(dest="command")

    solveC = subparsers.add_parser("solve", help="Решение уравнения", allow_abbrev=False)

    solveC.add_argument("-a", type=int, help="Коэффициент A")
    solveC.add_argument("-b", type=int, help="Коэффициент B")
    solveC.add_argument("-c", type=int, help="Коэффициент C")

    statsC = subparsers.add_parser("stats", help="Читает числа, вычисляет и выводит одиннадцать показателей\nКоличество чисел — не более 20, сами числа вещественные и конечные, по модулю не превышающие 10 000.\nЗначения NaN и бесконечности недопустимы.",
     allow_abbrev=False)

    statsC.add_argument("--input", help="Задаёт имя файла, из которого читаются числа")


    return parser


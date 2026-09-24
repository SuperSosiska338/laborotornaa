import argparse

def commandos():
    parser = argparse.ArgumentParser(prog="mathtool", description=
"mathtool — позволяет выполнять расчёты над уравнениями и числовыми последовательностями",
 allow_abbrev=False)

    subparsers = parser.add_subparsers(dest="command")

    solveC = subparsers.add_parser("solve", help="Решение уравнения", allow_abbrev=False)

    solveC.add_argument("-a", type=int, help="Коэффициент A:\nцелые, по модулю не более 10 000")
    solveC.add_argument("-b", type=int, help="Коэффициент B:\nцелые, по модулю не более 10 000")
    solveC.add_argument("-c", type=int, help="Коэффициент C:\nцелые, по модулю не более 10 000")

    statsC = subparsers.add_parser("stats", help="Читает числа, вычисляет и выводит одиннадцать показателей\nКоличество чисел — не более 20, сами числа вещественные и конечные, по модулю не превышающие 10 000.\nЗначения NaN и бесконечности недопустимы.",
     allow_abbrev=False)

    statsC.add_argument("--input", help="Задаёт имя файла, из которого читаются числа")

    seriesC = subparsers.add_parser("series", help="Выводит формулу ряда, вычисляет и выводит его сумму",
     allow_abbrev=False)

    seriesC.add_argument("--func", required=True, help="Задаёт какой ряд суммировать")

    FUNCargument = seriesC.add_mutually_exclusive_group(required=True)
    FUNCargument.add_argument("--terms", type=int, help="Задаёт сколько слагаемых сложить:\nостановка по количеству. Целое от 1 до 10 000")
    FUNCargument.add_argument("--eps", type=float, help="Задаёт до какой величины слагремого считать:\nостановка по точности. Конечное число: больше нуля и не грубее 0,0001")


    integrateC = subparsers.add_parser("integrate", help="численное интегрирование функции", allow_abbrev=False)

    integrateC.add_argument("--func", required=True, help="имя интегрируемой функции")
    integrateC.add_argument("--from",type=float, dest="a", required=True, help="нижний предел")
    integrateC.add_argument("--to", type=float, dest="b", required=True, help="верхний предел")
    integrateC.add_argument("--steps", type=int, required=True, help="количество шагов")
    
    return parser


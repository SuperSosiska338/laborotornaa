import argparse

def commandos():
    argparse.ArgumentParser(prog="mathtool")

    subparsers = parser.add_subparsers(dest="command")

    solveC = subparsers.add_parser("solve", allow_abbrev=False)

    solveC.add_argument("-a", type=int)
    solveC.add_argument("-b", type=int)
    solveC.add_argument("-c", type=int)

    return command


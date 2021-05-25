"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import operator
import math
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

# parser.add_argument('func', type=str, help="Use only *, /, +, -")
parser.add_argument('func', type=str, help="Use only *, /, +, -")
parser.add_argument('arguments', nargs='+')

def calculate(args):
    func = args.func
    string_math = 'math.' + func + '(' + ','.join(args.arguments[:]) + ')'
    string_operator = 'operator.' + func + '(' + ','.join(args.arguments[:]) + ')'
    if func in dir(math):
        return eval(string_math)
    elif func in dir(operator):
        return eval(string_operator)
    raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()

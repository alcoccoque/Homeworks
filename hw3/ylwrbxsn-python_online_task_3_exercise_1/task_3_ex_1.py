"""Task 1
For a given integer n calculate the value which is equal to a:
- squared number, if its value is strictly positive;
- modulus of a number, if its value is strictly negative;
- zero, if the integer n is zero.

Example,
n = 4 result = 16
n = -5 result = 5
n = 0 result = 0

Example of how the task should be called:
python3 task_3_ex_1.py 4

Note: use argparse module for parsing arguments from CLI
"""
import argparse
from math import sqrt


def calculate(args):
    if args < 0:
        return abs(args)
    elif args == 0:
        return 0
    # elif (sqrt_num := sqrt(args)) ** 2 == args:
    return args ** 2
    # raise ValueError



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=float, help="capacity")
    args = parser.parse_args()
    print(calculate(args.n))


if __name__ == '__main__':
    main()

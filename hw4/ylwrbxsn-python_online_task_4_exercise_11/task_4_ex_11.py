"""
Write a function `fibonacci_loop(seq: list)`, which accepts a list of values and
prints out values in one line on these conditions:
 - floating point numbers should be ignored
 - string values should stop the iteration
 - loop control statements should be used

Example:
>>> fibonacci_loop([0, 1, 1.1, 1, 2, 99.9, 3, 0.0, 5, 8, "stop", 13, 21, 34])
0 1 1 2 3 5 8
"""
from math import sqrt


def fibonacci_loop(seq):
    val_lis = []
    for x in seq:
        if isinstance(x, int):
            val_lis.append(x)
        elif isinstance(x, float):
            pass
        else:
            break
    fib = lambda n: True if n == 0 or sqrt(5 * (n ** 2) - 4) % 1 == 0 or sqrt(5 * (n ** 2) + 4) % 1 == 0 else False
    val_lis = " ".join([str(x) for x in val_lis if fib(x)])
    print(val_lis)


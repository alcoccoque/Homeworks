"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""


def sum_binary_1(n: int):

    if isinstance(n, int) and int(n) > 0 and (x := (bin(int(n)).split('0b')[1]).count('1')):
        return x
    return None

print(sum_binary_1([123]))

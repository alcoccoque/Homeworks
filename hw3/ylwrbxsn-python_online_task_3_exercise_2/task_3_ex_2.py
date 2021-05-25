"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse



def from_roman_numerals(args):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    num = 0
    rnum = args.roman
    if all(x in rom_val for x in rnum):
        n = [rom_val[i] for i in rnum if i in rom_val]
        res = sum([i if i >= n[min(j + 1, len(n) - 1)] else -i for j, i in enumerate(n)])
        if 1 <= res <= 100:
            return res
    else:
        raise ValueError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('roman', type=str, help="capacity")
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()

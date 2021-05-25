""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse

SYMBOLS = '!"#$%&()*,./:;<=>?@[\]^_`{|}~'

def has_alpha(user_input, *args):
    user_input = user_input.replace('\'', '')
    for i in range(0, len(user_input) - 1):
        if user_input[i].isdigit() or user_input[i] in args:
            return False
        return True


def has_duplicate(user_input, *args):
    # loop on items except last one
    for i in range(0, len(user_input) - 1):
        # check for repeating operators like: '--', '++', '+-', '-+'
        if user_input[i] in args and user_input[i + 1] in args:
            return True
    return False


def calculate(user_input):
    user_input = user_input.replace('\'', '')
    nums = [""]
    for i in user_input:
        if i.isdigit():
            nums[-1] = nums[-1] + i
        else:
            nums.append(i)
    nums = [num for num in nums if num]
    result = sum(map(lambda x: int(x), nums))
    return result



def check_formula(user_input):
    if len(user_input) == 1 and user_input == '\'':
        return False, None
    if len(user_input) == 0:
        return False, None
    if user_input[0] == '-':
        return False, None
    if user_input == '\'\'':
        return False, None
    elif has_duplicate(user_input, '-', '+'):
        return False, None
    elif has_alpha(user_input, '-', '+'):
        return False, None
    else:
        try:
            return True, calculate(user_input)
        except ValueError:
            return False, None


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('user_input')
    args = parser.parse_args()
    # print(args.user_input)
    print(check_formula(args.user_input))
    print(check_formula(args.user_input))
    print(check_formula(args.user_input))



if __name__ == '__main__':
    main()

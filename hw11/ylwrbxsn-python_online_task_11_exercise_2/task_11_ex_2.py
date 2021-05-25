"""
Implement a decorator remember_result which remembers last result of function it decorates
and prints it before next call.

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
>>> "Last result = 'None'"
>>> "Current result = 'ab'"

sum_list("abc", "cde")
>>> "Last result = 'ab'"
>>> "Current result = 'abccde'"

sum_list(3, 4, 5)
>>> "Last result = 'abccde'"
>>> "Current result = '345'"
"""


def remember_result(fn):
    res = None
    def wrapper(*args):
        nonlocal res
        print(f"Last result = '{res}'")
        res = fn(*args)
        return res
    return wrapper

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result

# sum_list(15,20,15)
# sum_list(15,20,15,20)
# sum_list(15,20,15,30)
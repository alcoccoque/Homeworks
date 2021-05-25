"""
Task 3

Implement a decorator `call_once` which runs `sum_of_numbers` function once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

Example:
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

>>> 55

print(sum_of_numbers(999, 100))

>>> 55

print(sum_of_numbers(134, 412))

>>> 55
"""
def call_once(fn):
    res = 0
    def wrapper(*args):
        nonlocal res
        if res:
            return res
        else:
            res = fn(*args)
            return res
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

# print(sum_of_numbers(15,20))
# print(sum_of_numbers(15,25))
# print(sum_of_numbers(15,30))
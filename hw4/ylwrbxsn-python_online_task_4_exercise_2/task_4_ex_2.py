"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""

def is_palindrome(test_string: str) -> bool:
    if isinstance(test_string, str):
        val_str = [x.lower() for x in test_string if x.isalpha()]
        if all(x == val_str[-(i+1)] for i, x in enumerate(val_str)):
            return True
        return False
    raise ValueError

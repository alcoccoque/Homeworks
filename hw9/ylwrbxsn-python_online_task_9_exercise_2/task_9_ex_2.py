"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""

def is_palindrome(test_string: str) -> bool:
    if isinstance(test_string, str):
        test_string = ''.join([x.lower() for x in test_string if x.isalpha()])
        if test_string == ''.join(reversed(test_string)):
            return True
        return False
    raise ValueError

# print(is_palindrome('ASDdsa'))
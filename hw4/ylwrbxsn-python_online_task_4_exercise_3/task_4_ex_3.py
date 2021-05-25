"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str = 0) -> list:
    if isinstance(delimiter, str):
        res = []
        tmp = ''
        for i in str_to_split:
            if i != delimiter:
                tmp += i
            else:
                res.append(tmp)
                tmp = ''
        if tmp:
            res.append(tmp)
        return res
    raise ValueError

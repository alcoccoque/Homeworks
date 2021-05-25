"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""

def valid_dict(*args):
    for d in args:
        for v in d.values():
            if not isinstance(v, int):
                raise ValueError
        for k in d.keys():
            if not k.isalpha() or len(k) > 1:
                raise KeyError


def combine_dicts(*args):
    valid_dict(*args)
    res = {}
    for d in args:
        res.update(d)
    for i in res:
        res[i] = sum(d.get(i, 0) for d in args)
    return res

print(combine_dicts({'a': 100, 'b': 200}, {'a': 100, 'd': 200},{'c': 100, 'b': 300}))
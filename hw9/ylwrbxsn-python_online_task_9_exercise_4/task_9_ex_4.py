"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string


def chars_in_all(*strings):
    if len(strings) >= 2:
        chars_inall = set()
        uniquechars = set(''.join(strings))
        for i in uniquechars:
            if all(i if i in x else False for x in strings):
                chars_inall.add(i)
        return chars_inall
    raise ValueError


def chars_in_one(*strings):
    return set(''.join(strings))


def chars_in_two(*strings):
    if len(strings) >= 2:
        chars_inall = set()
        uniquechars = set(''.join(strings))
        for i in uniquechars:
            if len([i for x in strings if i in x]) >= 2:
                chars_inall.add(i)
        return chars_inall
    raise ValueError


def not_used_chars(*strings):
    strings = set(''.join([x.lower() for x in strings if x.isalpha()]))
    list_of_str = set()
    for i in string.ascii_lowercase:
        if i not in strings:
             list_of_str.add(i)
        else:
            continue
    return list_of_str

#
# print(chars_in_all('asd', 'asas','asd'))
# print(chars_in_one('asd', 'asdasdd','asdddd'))
# print(chars_in_two('asd', 'asas','bbbbbb'))
# print(not_used_chars('asd', 'asas','bbbbbb'))
# print()
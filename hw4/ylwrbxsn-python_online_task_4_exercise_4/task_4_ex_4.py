"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    indexes = [x for x in indexes if isinstance(x, int) and x > 0 and x < len(string)]
    res = []
    max = 0
    for x in indexes:
        if x > max:
            max = x
            res.append(x)
        else:
            continue
    if res:
        res = [0] + res
        return [string[i:j] for i, j in zip(res, res[1:] + [None]) if string[i:j]]
    return [string]

"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
        somestr = []
        for i in string:
            if i == '"':
                somestr.append("'")
            elif i == "'":
                somestr.append('"')
            else:
                somestr.append(i)
        return ''.join(somestr)

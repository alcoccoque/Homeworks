"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import string
from collections import Counter

def most_common_words(text, top_words):
    with open(f'{text}', 'r', encoding='utf8') as inpt:
        data = inpt.read()
        data = [word.strip(string.punctuation) for word in data.split()]
        count_dict = {}
        for i in data:
            if i in count_dict:
                count_dict[i] += data.count(i)
            else:
                count_dict[i] = data.count(i)
    return [x[0] for x in Counter(count_dict).most_common(top_words)]

# print(most_common_words('inputfile.txt', 3))
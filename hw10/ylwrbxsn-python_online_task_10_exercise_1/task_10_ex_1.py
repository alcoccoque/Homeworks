"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, which sorts names from
`file_path` and write them to a new file `output_file_path`. Each name should start with a new line as in the
following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""
import os

def sort_names(input_file_path: str, output_file_path: str) -> None:
    with open(f'{input_file_path}', 'r', encoding='utf8') as inpt:
        data = inpt.read()
        data = (sorted(data.split('\n')))

    with open(output_file_path, 'w') as writer:
        for row in data:
            if row:
                writer.write(row + os.linesep)
            else:
                continue

# sort_names('inputfile.txt', 'sorted')
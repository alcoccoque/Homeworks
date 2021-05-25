"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import argparse
import os
import stat
import fnmatch

def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    result = []
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, pattern):
            result.append(path + '/' + file)
    return result


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    for file_path in file_paths:
        print(file_path, stat.filemode(os.stat(file_path).st_mode))
    print(f"Found {len(file_paths)} file(s).")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help="path")
    parser.add_argument('-p', help="pattern")
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()

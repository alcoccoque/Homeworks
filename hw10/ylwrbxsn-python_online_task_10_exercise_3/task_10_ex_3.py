"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""

import csv
from operator import itemgetter

def get_top_performers(file_path: str, number_of_top_students: int = 5) -> list:
    with open(file_path, newline='') as file:
        csv_data = list(csv.reader(file, quoting = csv.QUOTE_ALL))
        csv_data = csv_data[1:]
        csv_data = [[i[0], int(i[1]), float(i[2])] for i in csv_data]
        csv_data = sorted(csv_data, key=itemgetter(2), reverse=True)
        return [x[0] for x in csv_data[:number_of_top_students] if x]

def write_students_age_desc(file_path: str, output_file: str) -> None:
    with open(file_path, newline='') as file:
        csv_data = list(csv.reader(file, quoting=csv.QUOTE_ALL))
        info = csv_data[0]
        csv_data = csv_data[1:]
        csv_data = [[i[0], int(i[1]), float(i[2])] for i in csv_data]
        csv_data = sorted(csv_data, key=itemgetter(1), reverse=True)
    with open(f'{output_file}', 'w', newline='') as wfile:
        writer = csv.writer(wfile, delimiter=',')
        writer.writerow(info)
        for row in csv_data:
            if row:
                writer.writerow(row)
            else:
                continue
# print(get_top_performers('students.csv', 3))
# write_students_age_desc('students.csv', 'out.csv')
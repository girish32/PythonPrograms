import csv
import itertools
with open('projload.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = itertools.izip(*[lines] * 2)
    with open('newfile1.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Name of Issue', 'Issue ID'))
            writer.writerows(grouped)
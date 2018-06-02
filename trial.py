import urllib2
import unicodecsv as csv
import os
import sys
import io
import time
import datetime
import sys
import re


def to_2d(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


with open('projload.txt', 'r') as f:
    x = f.read()
print x

req_text = x.split('Load')[1: -1]

data = []
for text in req_text:
    text = text.split('\n', 1)[1]
    for line in text.strip().splitlines():
        data.append([line])

# maindatatable = to_2d(data, 4)

from string import ascii_uppercase as LETTERS

with open('projload.txt') as f, open('output.csv', 'wb') as g:
    actual_date = f.readline().strip()
    while True:
        first_line = f.readline().strip()
        if not first_line:
            break
        second_line = f.readline().strip()
        third_line = f.readline().strip()
        fourth_line = f.readline().strip()
        the_time, noun, number = first_line.split(' ')
        number = int(number)
        letter = LETTERS[number]
        new_line = '%s1:%s %s %s %s2:%s %s3:%s %s4:%s %s5:%s' % (
        letter, the_time, noun, number, letter, second_line, letter, third_line, letter, fourth_line, letter,
        actual_date)
        print (new_line)

f.close()
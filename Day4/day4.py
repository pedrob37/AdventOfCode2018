# Advent of code: Day 4
# Part One
import numpy as np
import os
import re
from datetime import datetime

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day4')
lines = [line.rstrip('\n') for line in open('input.txt')]

# Define date format
date_format = "%Y-%m-%d %H:%M"
time1 = datetime.strptime(sorted_dates[0][0], date_format)

# Let's split into: date, time, info
date_list = []
for row in range(len(lines)):
    date_list.append(re.split('\[|] ', lines[row])[1:])
sorted_dates = sorted(date_list, key=lambda x: x[0])
# sorted(lines, key=lambda d: tuple(map(int, d[0].split('-'))))

# Time differences
d0 = date(*tuple(map(np.int, (re.split('-', sorted_dates[0][0][0:11])))))
d1 = date(*tuple(map(np.int, (re.split('-', sorted_dates[1000][0][0:11])))))
delta = d1 - d0
print(delta.days)

day_first = datetime.strptime(sorted_dates[0][0], date_format)
day_last = datetime.strptime(sorted_dates[-1][0], date_format)
num_days = day_last - day_first


class Guard:
    def __init__(self, info):
        date_format = "%Y-%m-%d %H:%M"
        self.date = datetime.strptime(info[0], date_format)
        self.text = re.split(' ', info[1])[0]

    def find_type(self):
        if 'Guard' in self.text:
            ID = re.split('#| |', string)[2]
            return ID
        else:
            month = self.date.month
            day = self.date.day
            time = self.date.minute
            state = self.text
            return month, day, time

    def 

info_box = []
for row in range(len(sorted_dates)):
    if sorted_dates[row][1][0] == 'G':
        
        info_box.append(sorted_dates[row][0][5:10] + )
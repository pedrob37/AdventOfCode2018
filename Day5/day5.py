# Advent of code: Day 5
# Part One
import numpy as np
import os
import time

start = time.time()
os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day5')
with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]
    lines_copy = [line.rstrip('\n') for line in f]


lines = list(lines[0])
for epoch in range(2000):
    lister = []
    counter = 0
    for letter in range(len(lines)):
        if counter == len(lines) - 1:
            lister.append(lines[counter])
        elif counter == len(lines):
            break
        elif (lines[counter].istitle() and lines[counter + 1] == lines[counter].lower()) or (not lines[counter].istitle() and lines[counter + 1] == lines[counter].upper()):
            counter += 1
        else:
            lister.append(lines[counter])
        counter += 1
    if lister == lines:
        print(len(lines))
        break
    else:
        lines = lister
end = time.time()
print(end - start)

# %% Part Two
import string
start = time.time()
alphabet = string.ascii_lowercase
collapse_nums = np.zeros(len(alphabet))
for unit in alphabet:
    conc_lines = [x for x in lines if x != unit]
    conc_lines = [x for x in conc_lines if x != unit.upper()]
    for epoch in range(5000):
        lister = []
        counter = 0
        for letter in range(len(conc_lines)):
            if counter == len(conc_lines) - 1:
                lister.append(conc_lines[counter])
            elif counter == len(conc_lines):
                break
            elif (conc_lines[counter].istitle() and conc_lines[counter + 1] == conc_lines[counter].lower()) or (not conc_lines[counter].istitle() and conc_lines[counter + 1] == conc_lines[counter].upper()):
                counter += 1
            else:
                lister.append(conc_lines[counter])
            counter += 1
        if lister == conc_lines:
            collapse_nums[alphabet.index(unit)] = len(conc_lines)
            break
        else:
            conc_lines = lister
end = time.time()
print(end - start)
print(np.min(collapse_nums))

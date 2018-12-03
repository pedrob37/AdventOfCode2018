# Advent of code: Day 3
# Part One
import numpy as np
import os
import re

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day3')
lines = [line.rstrip('\n') for line in open('input.txt')]

# Breakdown
# X, Y, W, H
spec_array = np.zeros([len(lines), 4], dtype=np.int16)
for row in range(len(lines)):
    split_list = re.split('@ |: |x|,', lines[row])
    spec_array[row, :] = [int(x) for x in split_list[1:]]

# Create large array (fabric square)
square = np.zeros([10000, 10000])
for row in range(len(lines)):
    spec_list = spec_array[row, :]
    X = spec_list[0]
    Y = spec_list[1]
    W = spec_list[2]
    H = spec_list[3]
    square[Y:Y+H, X:X+W] += 1

square[square == 1] = 0
overlap_count = np.count_nonzero(square)
print(overlap_count)

# %% Part Two: Overlapping squares
# How to know ID claim that remained un-overlapped?
# Assign each "sum" a power of two
# Summing powers of 2 =/= power of 2
#import copy
square = np.zeros([1000, 1000])
for row in range(len(lines)):
    spec_list = spec_array[row, :]
    X = spec_list[0]
    Y = spec_list[1]
    W = spec_list[2]
    H = spec_list[3]
    square[Y:Y+H, X:X+W] += 1

# Want to find the piece of fabric that only creates zeros when subtracted
zero_count = 1e6 - np.count_nonzero(square)
for row in range(len(lines)):
    # square_copy = copy.deepcopy(square)
    spec_list = spec_array[row, :]
    X = spec_list[0]
    Y = spec_list[1]
    W = spec_list[2]
    H = spec_list[3]
    area = W * H
    square[Y:Y+H, X:X+W] -= 1
    new_zero_count = 1e6 - np.count_nonzero(square)
    if new_zero_count - zero_count == area:
        print(row + 1)
    square[Y:Y+H, X:X+W] += 1

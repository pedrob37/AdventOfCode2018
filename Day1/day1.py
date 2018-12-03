# Advent of code: Day 1
# Part One
import numpy as np
import os

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day1')
lines = [line.rstrip('\n') for line in open('input.txt')]
frequencies = [np.int(frequency) for frequency in lines]
net_frequency = np.sum(frequencies)
print(net_frequency)

# %% Part Two: 481, 141 seconds
# import time
# start = time.time()
current_freq = 0
net_list = set()
net_list.add(current_freq)

for epoch in range(np.int(1e6)):
    for frequency in frequencies:
        current_freq += frequency
        if (current_freq in net_list):
            print(current_freq)
            break
        if epoch == 0:
            net_list.add(current_freq)
    else:
        continue
    break
# end = time.time()
# print(end - start)

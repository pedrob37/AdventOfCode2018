# Advent of code: Day 2
# Part One
import numpy as np
import os

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day2')
IDs = [line.rstrip('\n') for line in open('input.txt')]

# Start counter for each of the checksums: i.e.: IDs with letter duplicates and
# IDs with letter triplicates
checksum_2 = 0
checksum_3 = 0
for ID in IDs:
    # Find the unique letters in each ID ('list' splits string into components)
    uniques = np.unique(list(ID))
    # For each unique letter want to know how many times it shows up
    unique_counter = np.zeros(len(uniques))
    for char in range(len(uniques)):
        # Count how many times each letter features in the ID
        # and save the value
        unique_counter[char] = ID.count(uniques[char])
    # If there is at least one letter that shows up twice,
    # add one to checksum_2
    if 2 in unique_counter:
        checksum_2 += 1
    # If there is at least one letter that shows up thrice,
    # add one to checksum_3
    if 3 in unique_counter:
        checksum_3 += 1
# Multiply the counts to calculate the final checksum
print(checksum_2 * checksum_3)

# %% Part Two
# Need to find the two strings that differ by exactly ONE character, in the
# same position. E.g.: ghyui & ghkui, and find the letters they have in common
ID_length = len(IDs[0])
for string in range(len(IDs)):
    exc_IDs = IDs[:string] + IDs[string+1:]
    for comp_str in exc_IDs:
        counter = 0
        shared_ID = []
        for let1, let2 in zip(IDs[string], comp_str):
            if let1 == let2:
                counter += 1
                shared_ID.append(let1)
        if counter == 25:
            print(IDs[string], comp_str)
            print(''.join(shared_ID))
            break
    else:
        continue
    break

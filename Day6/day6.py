# Advent of code: Day 6
# Part One
import os
import numpy as np
import re
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day6')
with open('input.txt', 'r') as f:
    coords = [line.rstrip('\n') for line in f]

coords_array = np.zeros([len(coords), 2], dtype=np.int16)
for index, entry in enumerate(coords):
    coords_array[index, :] = re.split(',', entry)


def manhattan(mat_coord, ref_coord):
    return sum([abs(mat_coord[i]-ref_coord[i]) for i in range(len(mat_coord))])


def assign_coord(mat_coord, ref_coords):
    num_coords = ref_coords.shape[0]
    manhattan_scores = np.zeros([num_coords])
    for index in range(num_coords):
        manhattan_scores[index] = manhattan(mat_coord, ref_coords[index, :])
    closests = np.argwhere(manhattan_scores == np.amin(manhattan_scores))
    if len(closests) > 1:
        return -1
    else:
        return np.argmin(manhattan_scores)


# Create empty grid
mat_coords = np.zeros([400,
                       400])

# Calculate the min Manhattan distance at each point
for i in range(mat_coords.shape[0]):
    print(i)
    for j in range(mat_coords.shape[1]):
        mat_coord = np.array([i, j])
        mat_coords[i, j] = assign_coord(mat_coord, coords_array)
plt.imshow(mat_coords)

# %%
# Want to know which reference coordinates "touch" the edges: These will have
# Infinite areas

excludes = np.unique([mat_coords[0, :], mat_coords[:, 0],
                      mat_coords[-1, :], mat_coords[:, -1]])
for exclude in excludes:
    mat_coords[mat_coords == exclude] = -1

plt.imshow(mat_coords)

# %% Count
unique, counts = np.unique(mat_coords, return_counts=True)

counts = np.dstack((unique, counts))
counts = counts.squeeze()

print(np.max(counts[1:, 1]))


# %% Part 2: Manhattan Sums
def assign_sum(mat_coord, ref_coords):
    num_coords = ref_coords.shape[0]
    manhattan_sum = 0
    for index in range(num_coords):
        manhattan_sum += manhattan(mat_coord, ref_coords[index, :])
    return manhattan_sum


# Create empty grid
mat_sums = np.zeros([400,
                     400])

# Calculate the Manhattan sums at each point
for i in range(mat_sums.shape[0]):
    print(i)
    for j in range(mat_sums.shape[1]):
        mat_coord = np.array([i, j])
        mat_sums[i, j] = assign_sum(mat_coord, coords_array)
plt.imshow(mat_sums)

# Calculate size of area < 10000
mat_sums[mat_sums < 10000] = 1
mat_sums[mat_sums >= 10000] = 0
print(np.sum(mat_sums))

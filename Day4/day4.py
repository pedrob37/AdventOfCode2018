# Advent of code: Day 4
# Part One
import numpy as np
import os
import re
from datetime import datetime
from scipy import stats

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day4')
lines = [line.rstrip('\n') for line in open('input.txt')]

# Let's split into: date, time, info
date_list = []
for row in range(len(lines)):
    date_list.append(re.split('\[|] ', lines[row])[1:])
sorted_dates = sorted(date_list, key=lambda x: x[0])

# %%
date_format = "%Y-%m-%d %H:%M"
tot_days = (datetime.strptime(sorted_dates[-1][0], date_format) -
            datetime.strptime(sorted_dates[0][0], date_format)).days + 1
timings = np.zeros([tot_days, 62], dtype=np.uint16)  # Date then guard #
day_ind = -1
for index, entry in enumerate(sorted_dates):
    date = datetime.strptime(entry[0], date_format)
    text = re.split(' ', entry[1])
    if 'Guard' in text:
        if index != 0:
            timings[day_ind, prev_tracker+2:] = 0
        day_ind += 1
        if date.hour == 23:
            day = date.day + 1
        else:
            day = date.day
        timings[day_ind, 0] = day
        ID = text[1][1:]
        timings[day_ind, 1] = ID
        prev_tracker = 0
    elif 'falls' in text:
        minute = date.minute
        timings[day_ind, prev_tracker+2:minute+2] = 0
        prev_tracker = minute
    elif 'wakes' in text:
        minute = date.minute
        timings[day_ind, prev_tracker+2:minute+2] = 1
        prev_tracker = minute

# %%
# Need to find minute MODE NOT TOTAL
guard_ids = list(np.unique(timings[:, 1]))
guard_tots = np.zeros([len(guard_ids)])
for day in range(tot_days):
    current_id = timings[day, 1]
    guard_tots[guard_ids.index(current_id)] += np.sum(timings[day, 2:])
guard_tots = list(guard_tots)
bad_guard = guard_ids[guard_tots.index(max(guard_tots))]

minutes = []
for day in range(tot_days):
    current_id = timings[day, 1]
    if current_id == bad_guard:
        for minute in range(60):
            if timings[day, minute+2] == 1:
                minutes.append(minute)
minutes_mode, _ = stats.mode(minutes)
print(int(minutes_mode)*bad_guard)

# %% Part Two: Find guard that falls asleep on the same minute most often
date_format = "%Y-%m-%d %H:%M"
tot_days = (datetime.strptime(sorted_dates[-1][0], date_format) -
            datetime.strptime(sorted_dates[0][0], date_format)).days + 1
timings = np.zeros([tot_days, 62], dtype=np.uint16)  # Date then guard #
day_ind = -1
for index, entry in enumerate(sorted_dates):
    date = datetime.strptime(entry[0], date_format)
    text = re.split(' ', entry[1])
    if 'Guard' in text:
        if index != 0:
            timings[day_ind, prev_tracker+2:] = 1e5*np.random.rand()
        day_ind += 1
        if date.hour == 23:
            day = date.day + 1
        else:
            day = date.day
        timings[day_ind, 0] = day
        ID = text[1][1:]
        timings[day_ind, 1] = ID
        prev_tracker = 0
    elif 'falls' in text:
        minute = date.minute
        timings[day_ind, prev_tracker+2:minute+2] = 1e5*np.random.rand()
        prev_tracker = minute
    elif 'wakes' in text:
        minute = date.minute
        timings[day_ind, prev_tracker+2:minute+2] = timings[day_ind, 1]
        prev_tracker = minute

minute_modes = np.zeros([60, 2])
best = np.array([0, 0, 0])
for minute in range(60):
    minute_mode, frequency = stats.mode(timings[:, minute+2])
    minute_modes[minute, :] = [int(minute_mode), int(frequency)]
    if int(frequency) > best[2]:
        best = [minute, int(minute_mode), int(frequency)]
print(best[0]*best[1])

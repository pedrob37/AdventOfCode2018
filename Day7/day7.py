# Advent of code: Day 7
# Part One
import numpy as np
import os

os.chdir(r'C:\Users\pedro\Desktop\AdventOfCode\Day7')
lines = [line.rstrip('\n') for line in open('input.txt')]

solution = []
preqs = []
posts = []
for epoch in range(2):
    # Do one run through the data to create list of "Pre-requisites" and
    # The actual steps (Posts)
    if epoch == 0:
        for entry in range(len(lines)):
            preqs.append(lines[entry][5])
            posts.append(lines[entry][36])
        # Want to find the starting step, i.e. the step that has no pre-req.
        # Can do this by finding which step does not have "Complete ... before
        # 'this' step, i.e. step which is a pre-req, but not a post-req
        temp_sol = []
        for preq in preqs:
            if preq not in posts:
                temp_sol.append(preq)
            candidates = list(np.unique(temp_sol))
        # There are a few steps with no pre-req, obviously pick the first
        solution.append(candidates[0])
    else:
        # 26 letters in the alphabet, already have the first => 26 - 1 - 1
        for entry in range(25):
            # Find all steps that have as pre-req the last step in the solution
            # (Only last because candidates is a running list)
            preq_matches = [posts[ind] for ind, preq in enumerate(preqs)
                            if preq == solution[-1]]
            # Pop the first entry because that was added to solution in last
            # iter (since it the the first alphabetically)
            candidates.pop(0)
            # Add all potential next steps to candidates
            candidates += preq_matches
            # Find uniques to sort and get rid of duplicates
            candidates = list(np.unique(candidates))
            # Create candidates 'copy'
            # Do this to avoid issues with popping lists that are being
            # iterated over
            real_candidates = []
            # Not enough to take first candidate, need to check for each
            # candidate if they have other unfulfilled pre-reqs
            for cand_ind, cand in enumerate(candidates):
                # Need to find what requirements the current candidates have
                cand_preqs = [preqs[ind] for ind, post in enumerate(posts)
                              if post == cand]
                cand_preqs = set(cand_preqs)
                solution_set = set(solution)
                # If all pre-reqs found in solution, then can proceed
                if solution_set.intersection(cand_preqs) == cand_preqs:
                    real_candidates.append(cand)
            # Finally, check if it already is a part of the solution: Only take
            # FIRST one, hence break chain if found
            for index, r_cand in enumerate(real_candidates):
                if real_candidates[index] not in solution:
                    break
            # Add this line just in case loop gets to end to avoid appending
            # final element (which already might be in solution)
            if real_candidates[index] not in solution:
                solution.append(real_candidates[index])
print(''.join(solution))

# %% Part 2
# Have four additional helpers: Steps can be worked on simultaneously
# As soon as pre-reqs can be met, step can be worked on

working_solution = {}  # i.e.: Work in progress
solution = []
preqs = []
posts = []

# Want to run simulation as a whole
for epoch in range(2):
    # Do one run through the data to create list of "Pre-requisites" and
    # The actual steps (Posts)
    if epoch == 0:
        for entry in range(len(lines)):
            preqs.append(lines[entry][5])
            posts.append(lines[entry][36])
        # Want to find the starting step, i.e. the step that has no pre-req.
        # Can do this by finding which step does not have "Complete ... before
        # 'this' step, i.e. step which is a pre-req, but not a post-req
        temp_sol = []
        for preq in preqs:
            if preq not in posts:
                temp_sol.append(preq)
            candidates = list(np.unique(temp_sol))
        # Because there are multiple workers, add them all to WIP
        for candidate in candidates:
            # Need to check we don't have more WIP steps than workers
            if len(working_solution) < 5:
                # Because the second a worker starts working on a step counts,
                # Start 'progress' at 1
                working_solution[candidate] = 1
    else:
        # Set upper limit to approx. time taken if only had one worker ~ 2340
        for sec in range(26*ord('Z')):
            # Loop over WIP steps
            for key in list(working_solution):
                # If step completed, it is no longer a WIP, so move it to
                # solutions and remove it from working_solution
                if working_solution[key] == (ord(key) - 4):
                    solution.append(key)
                    working_solution.pop(key)
                # Else, work on it for current second
                else:
                    working_solution[key] += 1
            if solution:
                preq_matches = [posts[ind] for ind, preq in enumerate(preqs)
                                if preq == solution[-1]]
                # Pop the first entry because that was added to solution in
                # last iter (since it the the first alphabetically)
                candidates.pop(0)
                # Add all potential next steps to candidates
                candidates += preq_matches
                # Find uniques to sort and get rid of duplicates
                candidates = list(np.unique(candidates))
                # Create candidates 'copy'
                # Do this to avoid issues with popping lists that are being
                # iterated over
                real_candidates = []
                accep_candidates = []
                # Not enough to take first candidate, need to check for each
                # candidate if they have other unfulfilled pre-reqs
                for cand_ind, cand in enumerate(candidates):
                    # Need to find what reqs the current candidates have
                    cand_preqs = [preqs[ind] for ind, post in enumerate(posts)
                                  if post == cand]
                    cand_preqs = set(cand_preqs)
                    solution_set = set(solution)
                    # If all pre-reqs found in solution, then can proceed
                    if solution_set.intersection(cand_preqs) == cand_preqs:
                        real_candidates.append(cand)
                # Finally, check if it already is a part of the solution
                # Append it to a list instead of breaking (as before) since can
                # now work on multiple solns at once
                for index, r_cand in enumerate(real_candidates):
                    if real_candidates[index] not in solution:
                        if real_candidates[index] not in working_solution:
                            accep_candidates.append(real_candidates[index])
                # Add as many accep_candidates as number of workers allows
                for accep_cand in accep_candidates:
                    if len(working_solution) < 5:
                        working_solution[accep_cand] = 1
            if len(solution) == 26:
                break
# Voila, add one because seconds begin counting at zero
print(solution, sec+1)

import string
alphabet = string.ascii_lowercase
line = open("input.txt").read().splitlines()[0]

lister = []
while lister != line:
    lister = line
    for letter_ind in range(len(alphabet)):
        line = line.replace(alphabet[letter_ind] + alphabet[letter_ind].upper(), "")
        line = line.replace(alphabet[letter_ind].upper() + alphabet[letter_ind], "")

#print("Part1:")
#print(len(line))

original = line
best = len(line)
for repl_letter in range(len(alphabet)):
    line = original
    line = line.replace(alphabet[letter_ind], "")
    line = line.replace(alphabet[letter_ind].upper(), "")
    oldline = None
    while oldline != line:
        oldline = line
        for letter in range(len(alphabet)):
            line = line.replace(alphabet[letter_ind] + alphabet[letter_ind].upper(), "")
            line = line.replace(alphabet[letter_ind].upper() + alphabet[letter_ind], "")

    best = len(line) if len(line) < best else best
#print("Part2:")
#print(best)
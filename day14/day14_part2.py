#!/usr/bin/env python3

with open("input.txt", "r") as f:
    original_template = f.readline().rstrip()
    f.readline()    # skip empty line
    d = {}
    for line in f:
        split = line.rstrip().split()
        d[split[0]] = split[2]

perms_20 = {}
counts_20 = {}
for perm in d:
    template = perm
    for _ in range(20):
        polymer = ""
        for i in range(len(template)-1):
            polymer += f"{template[i]}{d[template[i:i+2]]}"
        polymer += template[-1]
        template = polymer
    perms_20[perm] = polymer[:-1]
    counts = {}
    for x in polymer[:-1]:
        counts[x] = counts[x]+1 if x in counts else 1
    counts_20[perm] = counts

# Get polymer after 20 steps
polymer = ""
for j in range(len(original_template)-1):
    pair = original_template[j:j+2]
    polymer += perms_20[pair]
polymer += original_template[-1]

# Get counts after 20 more steps (20 + 20 = 40)
occurences = {x:0 for x in set(original_template)}
template = polymer
for i in range(len(template)-1):
    pair = template[i:i+2]
    counts = counts_20[pair]
    occurences = {k: occurences.get(k, 0) + counts.get(k, 0) for k in set(original_template)}
occurences[original_template[-1]] += 1
print(max(occurences.values())-min(occurences.values()))

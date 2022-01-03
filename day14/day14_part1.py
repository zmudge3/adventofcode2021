#!/usr/bin/env python3

with open("input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()    # skip empty line
    d = {}
    for line in f:
        split = line.rstrip().split()
        d[split[0]] = split[2]

for _ in range(10):
    polymer = ""
    for i in range(len(template)-1):
        polymer += f"{template[i]}{d[template[i:i+2]]}"
    polymer += template[-1]
    template = polymer

occurences = {}
for x in polymer:
    occurences[x] = occurences[x]+1 if x in occurences else 1
print(max(occurences.values())-min(occurences.values()))

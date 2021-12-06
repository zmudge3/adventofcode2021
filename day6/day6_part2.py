#!/usr/bin/env python3

with open("input.txt", "r") as f:
    l = [int(x) for x in f.readline().rstrip().split(",")]

d = {x:0 for x in range(9)}
for x in l:
    d[x] += 1

for i in range(256):
    copy = dict(d)
    for k in [0,1,2,3,4,5,7]:
        d[k] = copy[k+1]
    d[6] = copy[7] + copy[0]
    d[8] = copy[0]

print(sum(d.values()))
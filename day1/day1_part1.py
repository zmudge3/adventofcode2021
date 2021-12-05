#!/usr/bin/env python3

with open("input.txt", "r") as f:
    count = 0
    prev = int(f.readline().rstrip())
    for line in f:
        curr = int(line.rstrip())
        if curr > prev:
            count += 1 
        prev = curr

print(count)
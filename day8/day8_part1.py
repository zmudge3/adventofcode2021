#!/usr/bin/env python3

with open("input.txt", "r") as f:
    l = []
    for line in f:
        l += line.split("|")[1].split()

print(len(list(filter(lambda x: len(x) in [2,3,4,7], l))))

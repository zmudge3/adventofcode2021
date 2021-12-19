#!/usr/bin/env python3

# Because why not!
with open("input.txt", "r") as f:
    print(len(list(filter(lambda x: len(x) in [2,3,4,7], [el for line in f for el in line.split("|")[1].split()]))))

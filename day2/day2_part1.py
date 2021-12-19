#!/usr/bin/env python3

with open("input.txt", "r") as f:
    h_pos = 0
    depth = 0
    for line in f:
        split = line.rstrip().split(" ")
        move,dist = split[0],int(split[1])
        if move == "forward":
            h_pos += dist
        elif move == "up":
            depth = max(0, depth-dist)
        else:
            depth += dist

print(depth*h_pos)

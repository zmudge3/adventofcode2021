#!/usr/bin/env python3

with open("input.txt", "r") as f:
    h_pos = 0
    depth = 0
    aim = 0
    for line in f:
        split = line.rstrip().split(" ")
        move,dist = split[0],int(split[1])
        if move == "forward":
            h_pos += dist
            depth += aim*dist
        elif move == "up":
            aim = max(0, aim-dist)
        else:
            aim += dist

print(h_pos*depth)
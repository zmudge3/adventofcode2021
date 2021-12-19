#!/usr/bin/env python3

with open("input.txt", "r") as f:
    l = [line.rstrip() for line in f]

low_points = []
for i in range(len(l)):
    curr_line = l[i]
    for j in range(len(curr_line)):
        adjacent = []
        if i == 0:  # first line
            adjacent.append(l[i+1][j])
        elif i == len(l)-1: # last line
            adjacent.append(l[i-1][j])
        else:
            adjacent.append(l[i+1][j])
            adjacent.append(l[i-1][j])
        
        if j == 0:
            adjacent.append(curr_line[j+1])
        elif j == len(curr_line)-1:
            adjacent.append(curr_line[j-1])
        else:
            adjacent.append(curr_line[j+1])
            adjacent.append(curr_line[j-1])

        if list(set([curr_line[j] < x for x in adjacent])) == [True]:
            low_points.append(curr_line[j])

print(sum([int(x)+1 for x in low_points]))

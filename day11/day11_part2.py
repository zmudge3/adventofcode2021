#!/usr/bin/env python3

def get_adjacents(i,j):
    adjacents = []
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if x not in [-1,10] and y not in [-1,10] and (x,y) != (i,j):
                adjacents.append((x,y))
    return adjacents

with open("input.txt", "r") as f:
    d = {}
    num = 0
    for line in f:
        line = line.rstrip()
        for i in range(len(line)):
            d[(num,i)] = int(line[i])
        num += 1

steps = 0
while True:
    for el in d:
        d[el] += 1
    flashes = []
    stack = [k for k,v in d.items() if v == 10]
    for el in stack:
        flashes.append(el)
        d[el] = 0
    while len(stack) > 0:
        i,j = stack.pop()
        adjacents = get_adjacents(i,j)
        for adj_i,adj_j in adjacents:
            if (adj_i,adj_j) not in flashes:
                d[(adj_i,adj_j)] += 1
                if d[(adj_i,adj_j)] == 10:
                    flashes.append((adj_i,adj_j))
                    d[(adj_i,adj_j)] = 0
                    stack.append((adj_i,adj_j))
    if list(d.values()) == [0]*100:
        print(f"Part 2: {steps}")
        break
    steps += 1

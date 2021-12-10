#!/usr/bin/env python3

with open("input.txt", "r") as f:
    l = [line.rstrip() for line in f]

def get_adjacents(l,i,j):
    adjacents = {}
    if i == 0:  # first line
        adjacents[(i+1,j)] = int(l[i+1][j])
    elif i == len(l)-1: # last line
        adjacents[(i-1,j)] = int(l[i-1][j])
    else:
        adjacents[(i+1,j)] = int(l[i+1][j])
        adjacents[(i-1,j)] = int(l[i-1][j])
    
    if j == 0:
        adjacents[(i,j+1)] = int(l[i][j+1])
    elif j == len(l[i])-1:
        adjacents[(i,j-1)] = int(l[i][j-1])
    else:
        adjacents[(i,j+1)] = int(l[i][j+1])
        adjacents[(i,j-1)] = int(l[i][j-1])
    return adjacents

def trace_basin(l,i,j):
    orig_i = i
    orig_j = j
    q = [(i,j)]
    results = []
    while len(q) > 0:
        i,j = q.pop()
        adjacents = get_adjacents(l,i,j)
        for k,v in adjacents.items():
            if (v != 9) and (v > int(l[i][j])):
                results.append(k)
                q = [k] + q
    return list(set(results)) + [(orig_i,orig_j)]
    
basin_lengths = []
for i in range(len(l)):
    for j in range(len(l[i])):
        adjacents = get_adjacents(l,i,j)
        if list(set([int(l[i][j]) < x for x in adjacents.values()])) == [True]: # if local min
            trace = trace_basin(l,i,j)
            basin_lengths.append(len(trace))

product = 1
for el in sorted(basin_lengths,reverse=True)[0:3]:
    product *= el
print(product)
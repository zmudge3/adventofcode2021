#!/usr/bin/env python3

def map_coords(coords,move):
    new_coords = set()
    if move[0] == 'x':
        for (x,y) in coords:
            if x > move[1]:
                new_coords.add((move[1]-(x-move[1]),y))
            else:
                new_coords.add((x,y))
    else:
        for (x,y) in coords:
            if y > move[1]:
                new_coords.add((x,move[1]-(y-move[1])))
            else:
                new_coords.add((x,y))
    return list(new_coords)

with open("input.txt", "r") as f:
    coords = []
    moves = []
    for line in f:
        line = line.rstrip()
        split = line.split(",")
        if len(split) > 1:
            coords.append((int(split[0]), int(split[1])))
        elif line == "":
            continue
        else:
            split = line.split()[2].split("=")
            moves.append((split[0],int(split[1])))

coords = map_coords(coords,moves[0])
print(len(coords))

#!/usr/bin/env python3

from fractions import Fraction

def calc_points(x1,y1,x2,y2):
    l = []
    if x1 == x2:
        if y1 > y2:
            temp_y = y2
            y2 = y1
            y1 = temp_y
        for y in range(y1,y2+1):
            l.append((x1,y))
    elif y1 == y2:
        if x1 > x2:
            temp_x = x2
            x2 = x1
            x1 = temp_x
        for x in range(x1,x2+1):
            l.append((x,y1))
    else:
        if x1 > x2:
            temp_x,temp_y = x2,y2
            x2,y2 = x1,y1
            x1,y1 = temp_x,temp_y
        slope = Fraction((y2-y1),(x2-x1))
        rise = slope.numerator
        run = slope.denominator
        l.append((x1,y1))
        x,y=x1,y1
        if y2 < y1:
            while x < x2 and y > y2:
                x += run
                y += rise
                l.append((x,y))
        else:
            while x < x2 and y < y2:
                x += run
                y += rise
                l.append((x,y))
    return l

with open("input.txt", "r") as f:
    d = {}
    for line in f:
        line = line.rstrip()
        coords1,coords2 = line.split(" -> ")
        coords = [int(x) for x in coords1.split(",")+coords2.split(",")]
        points = calc_points(coords[0],coords[1],coords[2],coords[3])
        for point in points:
            if point in d:
                d[point] += 1
            else:
                d[point] = 1

print(sum(value >= 2 for value in d.values()))
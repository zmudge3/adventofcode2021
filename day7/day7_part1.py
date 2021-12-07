#!/usr/bin/env python3

with open("input.txt", "r") as f:
    l = [int(pos) for pos in f.readline().rstrip().split(",")]

min_fuel = sum([abs(x-max(l)) for x in l])
for i in range(min(l), max(l)):
    fuel = sum([abs(x-i) for x in l])
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
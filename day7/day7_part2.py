#!/usr/bin/env python3

with open("input.txt", "r") as f:
    l = [int(pos) for pos in f.readline().rstrip().split(",")]

min_fuel = sum([sum(range(abs(x-max(l))+1)) for x in l])
for i in range(min(l), max(l)):
    fuel = sum([sum(range(abs(x-i)+1)) for x in l])
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)

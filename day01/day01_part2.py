#!/usr/bin/env python3

with open("input.txt", "r") as f:
    count = 0
    window = [int(f.readline().rstrip()) for _ in range(3)]
    prev_wind_sum = sum(window) 
    for line in f:
        del window[0]
        window.append(int(line.rstrip()))
        wind_sum = sum(window)
        if wind_sum > prev_wind_sum:
            count += 1
        prev_wind_sum = wind_sum

print(count)

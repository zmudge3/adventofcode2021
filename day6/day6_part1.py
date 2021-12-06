#!/usr/bin/env python3

def next_timers(timers):
    return [(timer-1) % 7 if timer <= 6 else timer-1 for timer in timers] + [8]*timers.count(0)

with open("input.txt", "r") as f:
    l = [int(x) for x in f.readline().rstrip().split(",")]

for i in range(81):
    print(i)
    print(len(l))
    l = next_timers(l)
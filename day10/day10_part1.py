#!/usr/bin/env python3

matches = {
    "{" : "}",
    "[" : "]",
    "<" : ">",
    "(" : ")"
}

scores = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

with open("input.txt", "r") as f:
    score = 0
    for line in f:
        line = line.rstrip()
        stack = []
        for el in line:
            if el in matches:
                stack.append(matches[el])
            elif el != stack.pop():
                score += scores[el]

print(score)
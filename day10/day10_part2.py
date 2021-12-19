#!/usr/bin/env python3

matches = {
    "{" : "}",
    "[" : "]",
    "<" : ">",
    "(" : ")"
}

scores = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

with open("input.txt", "r") as f:
    l = []
    for line in f:
        line = line.rstrip()
        stopped = False
        stack = []
        for el in line:
            if el in matches:
                stack.append(matches[el])
            elif el != stack.pop():
                stopped = True
                break
        
        if stopped == False:
            score = 0
            for c in list(reversed(stack)):
                score *= 5
                score += scores[c]
            l.append(score)

             
l_sorted = sorted(l)
print(l_sorted[len(l_sorted) // 2])

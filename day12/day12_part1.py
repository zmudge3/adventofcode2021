#!/usr/bin/env python3

def find_paths(adj_list):
    paths = []
    stack = [["start",x] for x in adj_list["start"]]
    while len(stack) > 0:
        l = stack.pop()
        last = l[-1]
        if last == "end":
            paths.append(l)
        else:
            for x in adj_list[last]:
                if x.islower():
                    if x not in l:
                        stack.append(l + [x])
                else:
                    stack.append(l + [x])
    return paths

with open("input.txt", "r") as f:
    adj_list = {}
    for line in f:
        a,b = line.rstrip().split("-")
        if a in adj_list:
            adj_list[a].add(b)
        else:
            adj_list[a] = {b}
        if b in adj_list:
            adj_list[b].add(a)
        else:
            adj_list[b] = {a}

print(len(find_paths(adj_list)))

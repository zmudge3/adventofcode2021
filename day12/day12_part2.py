#!/usr/bin/env python3

def find_paths(adj_list):
    lowers = list(filter(lambda x : x.islower() and x not in ["start", "end"], adj_list.keys()))
    paths = []
    stack = [["start",x] for x in adj_list["start"]]
    while len(stack) > 0:
        l = stack.pop()
        last = l[-1]
        if last == "end":
            paths.append(l)
        else:
            for el in adj_list[last]:
                d = {lower : 0 for lower in lowers}
                filtered = list(filter(lambda x : x.islower() and x not in ["start", "end"], l))
                for x in filtered:
                    d[x] += 1
                if el == "end":
                    stack.append(l + [el])
                elif el == "start" or (el.islower() and (2 in d.values() and d[el] in [1,2])):
                    continue
                else:
                    stack.append(l + [el])
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

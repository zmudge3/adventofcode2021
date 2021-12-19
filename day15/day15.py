#!/usr/bin/env python3

from queue import PriorityQueue

def dijkstra(lines):
    x_dim = len(lines[0])
    y_dim = len(lines)
    visited = set()
    D = {(i,j) : float('inf') for i in range(x_dim) for j in range(y_dim)}
    D[(0,0)] = 0

    pq = PriorityQueue()
    pq.put((0, (0,0)))

    while not pq.empty():
        dist,current_vertex = pq.get()
        visited.add(current_vertex)
        i,j = current_vertex
        for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if x not in [-1,x_dim] and y not in [-1,y_dim]:
                distance = int(lines[y][x])
                if (x,y) not in visited:
                    old_cost = D[(x,y)]
                    new_cost = D[(i,j)] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, (x,y)))
                        D[(x,y)] = new_cost

    return D[(x_dim-1,y_dim-1)]        

def expand_down(lines,nrows):
    new_rows = []
    for i in range(nrows):
        row = lines[-(nrows-i)]
        new_row = "".join([str((int(c)%9) + 1) for c in row])
        new_rows.append(new_row)
    return lines + new_rows

def expand_right(lines,ncols):
    new_cols = []
    for line in lines:
        chrs = line[-ncols:]
        new_chrs = "".join([str((int(c)%9) + 1) for c in chrs])
        new_cols.append(new_chrs)
    return [x+y for x,y in zip(lines,new_cols)]

        
with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

print(f"Part 1: {dijkstra(lines)}")

x_dim = len(lines[0])
y_dim = len(lines)
for _ in range(4):
    lines = expand_down(lines,x_dim)
for _ in range(4):
    lines = expand_right(lines,y_dim)

print(f"Part 2: {dijkstra(lines)}")

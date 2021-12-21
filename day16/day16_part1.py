#!/usr/bin/env python3

def parse_literal_pkt(remaining, version_sum):
    while remaining[0] == "1":
        remaining = remaining[5:]
    remaining = remaining[5:]
    return (remaining, version_sum)

def parse_operator_pkt(remaining, version_sum):
    length_type_id = remaining[0]
    remaining = remaining[1:]
    if length_type_id == "1":
        num_subpackets = int(remaining[:11],2)
        remaining = remaining[11:]
        remaining,version_sum = parse_subpackets_2(remaining, num_subpackets, version_sum)
    else:
        len_subpackets = int(remaining[:15],2)
        remaining = remaining[15:]
        remaining,version_sum = parse_subpackets_1(remaining, len_subpackets, version_sum)

    return (remaining, version_sum)

def parse_subpackets_1(remaining, len_subpackets, version_sum):
    i = 0
    while i < len_subpackets:
        version = remaining[:3]
        version_sum += int(version,2)
        type_id = remaining[3:6]
        remaining = remaining[6:]
        pre_length = len(remaining)
        if type_id == '100': # literal value pkt
            remaining,version_sum = parse_literal_pkt(remaining, version_sum)
        else:
            remaining,version_sum = parse_operator_pkt(remaining, version_sum)
        i += (pre_length - len(remaining)) + 6
    return (remaining, version_sum)

def parse_subpackets_2(remaining, num_subpackets, version_sum):
    subpackets_visited = 0
    while subpackets_visited < num_subpackets:
        version = remaining[:3]
        version_sum += int(version,2)
        type_id = remaining[3:6]
        remaining = remaining[6:]
        if type_id == '100': # literal value pkt
            remaining,version_sum = parse_literal_pkt(remaining, version_sum)
        else:
            remaining,version_sum = parse_operator_pkt(remaining, version_sum)
        subpackets_visited += 1
    return (remaining, version_sum)
        
with open("input.txt", "r") as f:
    h = f.readline().rstrip()

b = bin(int(h, 16))[2:].zfill(len(h)*4)
version = b[:3]
version_sum = int(version,2)
remaining = b[6:]
print(parse_operator_pkt(remaining, version_sum)[1])

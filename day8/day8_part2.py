#!/usr/bin/env python3

def solve(signals, output_list, signals_number):
    mapping = {}
    number_signals = {}
    number_signals["1"] = list(filter(lambda x: len(x) == 2, signals))[0]
    number_signals["4"] = list(filter(lambda x: len(x) == 4, signals))[0]
    number_signals["7"] = list(filter(lambda x: len(x) == 3, signals))[0]
    number_signals["8"] = list(filter(lambda x: len(x) == 7, signals))[0]

    mapping["a"] = (set(number_signals["7"])-set(number_signals["1"])).pop()
    len_6 = list(filter(lambda x: len(x) == 6, signals))
    for el in len_6:
        remaining = set(el)-set(number_signals["4"]+mapping["a"])
        if len(remaining) == 1:
            mapping["g"] = remaining.pop()
            number_signals["9"] = el
            break 
    mapping["e"] = (set(number_signals["8"])-set(number_signals["4"]+mapping["a"]+mapping["g"])).pop()
    len_5 = list(filter(lambda x: len(x) == 5, signals))
    for el in len_5:
        remaining = set(el) - set(mapping["a"]+mapping["e"]+mapping["g"])
        if len(remaining) == 2:
            number_signals["2"] = el
            break
    mapping["f"] = (set(number_signals["1"])-set(number_signals["2"])).pop()
    mapping["c"] = (set(number_signals["1"])-set(mapping["f"])).pop()
    mapping["d"] = (set(number_signals["2"])-set(mapping["a"]+mapping["c"]+mapping["e"]+mapping["g"])).pop()
    mapping["b"] = (set(number_signals["8"])-{v for v in mapping.values()}).pop()

    mapping = {v:k for k,v in mapping.items()}

    results = ""
    for el in output_list:
        results += signals_number["".join(sorted([mapping[c] for c in el]))]
    return(int(results))


signals_number = {
    "abcefg" : "0",
    "cf" : "1",
    "acdeg" : "2",
    "acdfg" : "3",
    "bcdf" : "4",
    "abdfg" : "5",
    "abdefg" : "6",
    "acf" : "7",
    "abcdefg" : "8",
    "abcdfg" : "9"
}

with open("input.txt", "r") as f:
    total = 0
    for line in f:
        split = line.split("|")
        signals,outputs = split[0].split(),split[1].split()
        total += solve(signals,outputs,signals_number)

print(total)
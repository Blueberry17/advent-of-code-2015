import itertools

raw_info = open("input.txt").read().split("\n")
info = {}
nodes = ""

for i in raw_info:
    parts = i.split()
    first, sign, points, second = parts[0][0], parts[2], int(parts[3]), parts[-1][0]
    if first not in info:
        nodes += first
        info[first] = {}
    if sign == "lose":
        info[first][second] = points*-1
    else:
        info[first][second] = points

combs = itertools.permutations(nodes, len(nodes))
best = float("-inf")
for comb in combs:
    total = 0
    for index in range(len(comb)-1):
        first, second = comb[index], comb[index+1]
        total += info[first][second] + info[second][first]
    first = comb[0]
    total += info[first][second] + info[second][first]
    if total > best:
        best = total

print(best)

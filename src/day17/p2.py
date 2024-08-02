import itertools

lines = open("input.txt").read().split("\n")
data = list(map(int, lines))
total = 0
minimum = float("inf")
for i in range(2, len(data)+1):
    for item in itertools.combinations(data, i):
        if sum(item) == 150:
            if i < minimum:
                minimum = i
                total += 1
            elif i == minimum:
                total += 1
print(total)

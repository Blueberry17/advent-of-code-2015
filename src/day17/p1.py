import itertools

lines = open("input.txt").read().split("\n")
data = list(map(int, lines))
total = 0
for i in range(2, len(data)+1):
    for item in itertools.combinations(data, i):
        if sum(item) == 150:
            total += 1
print(total)

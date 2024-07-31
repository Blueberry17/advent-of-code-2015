import itertools

lines = open("input.txt").read().split("\n")
items = ""
ingredients = []
for line in enumerate(lines):
    items += str(line[0])
    parts = line[1].split()
    ingredients.append(list(map(int, (parts[2][:-1], parts[4][:-1], parts[6][:-1], parts[8][:-1], parts[10]))))

combs = itertools.combinations_with_replacement(items, 100)
best = 0

for comb in combs:
    final = [0, 0, 0, 0, 0]
    for ingredient in comb:
        for part in enumerate(ingredients[int(ingredient)]):
            final[part[0]] += part[1]
    total = 1
    for i in final[:-1]:
        if i > 0:
            total *= i
        else:
            total = 0
    if total > best:
        best = total

print(best)

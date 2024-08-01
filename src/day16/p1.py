lines = open("input.txt").read().split("\n")

target = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]
aunts = []

for line in lines:
    parts = line.split()
    aunt = {"children": None, "cats": None, "samoyeds": None, "pomeranians": None, "akitas": None, "vizslas": None,
            "goldfish": None, "trees": None, "cars": None, "perfumes": None}
    for index in range(2, len(parts), 2):
        aunt[parts[index][:-1]] = int(parts[index+1].replace(",", ""))
    aunts.append(aunt)

    valid = True
    for index, value in enumerate(aunt.values()):
        if target[index] != value and value is not None:
            valid = False
    if valid:
        print(parts[1][:-1])

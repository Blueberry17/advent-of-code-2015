directions = open("day3info.txt").read()
places = set()
x1 = y1 = x2 = y2 = 0
for index, d in enumerate(directions):
    if index % 2 == 0:
        if d == ">":
            x1 += 1
        if d == "<":
            x1 -= 1
        if d == "^":
            y1 -= 1
        if d == "v":
            y1 += 1
        places.add((x1, y1))
    else:
        if d == ">":
            x2 += 1
        if d == "<":
            x2 -= 1
        if d == "^":
            y2 -= 1
        if d == "v":
            y2 += 1
        places.add((x2, y2))

print(len(places))

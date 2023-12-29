directions = open("input.txt").read()
places = set()
x1 = y1 = x2 = y2 = 0
for index, d in enumerate(directions.removesuffix("\n")):
    if index % 2 == 0:
        if d == ">":
            x1 += 1
        elif d == "<":
            x1 -= 1
        elif d == "^":
            y1 -= 1
        else:
            y1 += 1
        places.add((x1, y1))
    else:
        if d == ">":
            x2 += 1
        elif d == "<":
            x2 -= 1
        elif d == "^":
            y2 -= 1
        else:
            y2 += 1
        places.add((x2, y2))

print(len(places))

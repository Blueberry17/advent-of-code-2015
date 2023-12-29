directions = open("input.txt").read()
places = set()
x = y = 0
for d in directions.removesuffix("\n"):
    if d == ">":
        x += 1
    elif d == "<":
        x -= 1
    elif d == "^":
        y -= 1
    else:
        y += 1
    places.add((x, y))

print(len(places))

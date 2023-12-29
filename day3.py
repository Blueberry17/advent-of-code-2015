directions = open("day3info.txt").read()
places = set()
x = y = 0
for d in directions:
    if d == ">":
        x += 1
    if d == "<":
        x -= 1
    if d == "^":
        y -= 1
    if d == "v":
        y += 1
    places.add((x, y))

print(len(places))

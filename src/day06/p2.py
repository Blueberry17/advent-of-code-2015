import re

lights = []
for i in range(1000):
    lights.append([0] * 1000)

for line in open("input.txt").read().split("\n"):
    [op, x1, y1, x2, y2] = re.search(r'(\w+) (\d+),(\d+) through (\d+),(\d+)', line).groups()
    x1, y1, x2, y2 = tuple(map(int, (x1, y1, x2, y2)))

    if op == "on":
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                lights[y][x] += 1

    elif op == "off":
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                lights[y][x] = max(lights[y][x]-1, 0)

    else:
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                lights[y][x] += 2

total = 0
for y in range(1000):
    total += sum(lights[y])

print(total)

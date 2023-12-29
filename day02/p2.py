lines = open("input.txt").read().split("\n")
total = 0
for line in lines:
    x, y, z = tuple(map(int, line.split("x")))
    total += 2*(x+y+z) - 2*max(x, y, z) + x*y*z

print(total)

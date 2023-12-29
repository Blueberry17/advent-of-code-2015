lines = open("input.txt").read().split("\n")
total = 0
for line in lines:
    x, y, z = tuple(map(int, line.split("x")))
    total += 2*x*y + 2*x*z + 2*y*z + min(x*y, x*z, y*z)

print(total)

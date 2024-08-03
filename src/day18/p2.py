import copy

old = open("input.txt").read().split("\n")
for _ in range(100):
    new = []
    for y_index, y_val in enumerate(old):
        new_row = ""
        for x_index, x_val in enumerate(y_val):
            if x_index == 0 and y_index == 0 or x_index == len(old[0])-1 and y_index == 0 or \
                    x_index == len(old[0])-1 and y_index == len(old)-1 or x_index == 0 and y_index == len(old)-1:
                new_row += "#"
                continue
            total = 0
            if y_index < len(old)-1 and old[y_index+1][x_index] == "#":
                total += 1
            if y_index > 0 and old[y_index-1][x_index] == "#":
                total += 1
            if x_index < len(old[0])-1 and old[y_index][x_index+1] == "#":
                total += 1
            if x_index > 0 and old[y_index][x_index-1] == "#":
                total += 1
            if y_index < len(old)-1 and x_index < len(old[0])-1 and old[y_index+1][x_index+1] == "#":
                total += 1
            if y_index > 0 and x_index > 0 and old[y_index-1][x_index-1] == "#":
                total += 1
            if y_index > 0 and x_index < len(old[0])-1 and old[y_index-1][x_index+1] == "#":
                total += 1
            if y_index < len(old)-1 and x_index > 0 and old[y_index+1][x_index-1] == "#":
                total += 1
            if x_val == "#":
                if 2 <= total <= 3:
                    new_row += "#"
                else:
                    new_row += "."
            elif total == 3:
                new_row += "#"
            else:
                new_row += "."
        new.append(new_row)
    old = copy.deepcopy(new)
    new = []

lights = 0
for i in old:
    for j in i:
        if j == "#":
            lights += 1
print(lights)

brackets = open("day1info.txt").read()
total = 0
for index, i in enumerate(brackets):
    if i == "(":
        total += 1
    elif i == ")":
        total -= 1
    if total == -1:
        print(index)

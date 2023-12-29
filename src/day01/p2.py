brackets = open("input.txt").read()
total = 0
for index, i in enumerate(brackets):
    if i == "(":
        total += 1
    else:
        total -= 1
    if total == -1:
        print(index+1)
        break

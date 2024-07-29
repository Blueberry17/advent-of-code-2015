doc = open("input.txt").readline()

total = 0
previous = ""
neg = False
for char in doc:
    if char.isdigit():
        previous += char
    elif char == "-":
        neg = True
    else:
        if previous != "":
            if neg:
                total -= int(previous)
            else:
                total += int(previous)
            previous = ""
            neg = False

print(total)

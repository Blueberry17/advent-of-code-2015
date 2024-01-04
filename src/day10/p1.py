old = open("input.txt").readline()

for _ in range(40):
    new = ""
    last = ""
    count = 0

    for index, num in enumerate(old):
        if index == 0:
            last = num
            count = 1
        elif num == last:
            count += 1
        else:
            new += str(count) + last
            last = num
            count = 1
    new += str(count) + last

    if new != "":
        old = new

print(len(new))

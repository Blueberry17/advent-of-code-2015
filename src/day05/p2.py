total = 0

for line in open("input.txt").read().split("\n"):
    double_pair = split_double = False
    last = ""
    double_last = ""
    pairs = {}

    for index, char in enumerate(line):
        double_last += char
        if len(double_last) > 2 and double_last[-3] == double_last[-1]:
            split_double = True
        if len(last) > 0:
            if last+char in pairs.keys():
                if pairs[last+char] != index-1:
                    double_pair = True
            else:
                pairs[last+char] = index
            last = char
        else:
            last += char

    if double_pair and split_double:
        total += 1

print(total)

escaped_total = unescaped_total = 0
line_num = 0
for line in open("input.txt").read().split("\n"):
    line_num += 1
    escaped = line.replace(" ", "")

    escaped_length = 0
    unescaped_length = 0
    last = ""
    for index, char in enumerate(escaped):
        unescaped_length += 1
        escaped_length += 1

        if index == 0 or index == len(escaped)-1:
            escaped_length += 2
            if last == "\\":
                escaped_length += 1
            continue

        if last == "\\":
            last = ""
            if char == "\"":
                escaped_length += 2
            elif char == "\\":
                escaped_length += 1
                last = "\\"
            else:
                escaped_length += 1

        elif char == "\\":
            last += "\\"

    escaped_total += escaped_length
    unescaped_total += unescaped_length

    # print(line_num, unescaped_length, escaped_length)
    # print(escaped_length-unescaped_length)
    print(escaped_total - unescaped_total)

print(escaped_total - unescaped_total)

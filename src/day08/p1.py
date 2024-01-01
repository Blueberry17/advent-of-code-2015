escaped_total = unescaped_total = 0
for line in open("input.txt").read().split("\n"):
    escaped = line.replace(" ", "")

    escaped_length = 0
    unescaped_length = 0
    last = ""
    for index, char in enumerate(escaped):
        unescaped_length += 1
        if index == 0 or index == len(escaped)-1:
            continue

        if last.startswith("\\"):
            if char == "\\" or char == "\"" or len(last) == 3:
                escaped_length += 1
                last = ""
            else:
                last += char

        elif char == "\\":
            last += "\\"

        else:
            escaped_length += 1

    escaped_total += escaped_length
    unescaped_total += unescaped_length

print(unescaped_total - escaped_total)

doc = open("input.txt").readline()


def account(string):
    total = 0
    index = 0
    previous = ""
    neg = False
    null = False
    while index < len(string):
        char = string[index]

        if char == "{":
            to_add, index_change = account(string[index+1:])
            total += to_add
            index += index_change
        elif char == "}":
            if previous.isdigit():
                if neg:
                    total -= int(previous)
                else:
                    total += int(previous)
            if null:
                total = 0
            return total, index+1

        else:
            if char.isdigit():
                previous += char
            elif char == "-":
                neg = True
            elif index > 3 and string[index-4:index+1] == ":\"red":
                null = True
            else:
                if previous.isdigit():
                    if neg:
                        total -= int(previous)
                    else:
                        total += int(previous)
                    previous = ""
                    neg = False

        index += 1

    return total, index


print(account(doc))

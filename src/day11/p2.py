word = open("input.txt").readline()
alphabet = "abcdefghijklmnopqrstuvwxyz"


def next_value(value):
    value_list = []
    for i in value:
        value_list.append(alphabet.index(i))

    check_next = True
    index = -1
    while check_next:
        while True:
            value_list[index] = (value_list[index] + 1) % 26
            if value_list[index] not in [8, 11, 14]:
                break
        if value_list[index] != 0:
            check_next = False
        elif abs(index)+1 > len(value_list):
            index -= 1
            value_list.insert(0, 0)
            check_next = False
        else:
            index -= 1

    for char in value_list:
        yield alphabet[char]

score = 0
value = word
valid = False
while not valid:
    value = list(next_value(value))

    straight = 0
    last = ""
    banned = "iol"
    valid_straight = confusing = False
    valid_dupes = 0
    seen = ""
    for index, char in enumerate(value):
        if char in banned:
            confusing = True
            break
        if straight == 2:
            valid_straight = True
        if last != "" and alphabet.index(last) == alphabet.index(char)-1:
            straight += 1
        else:
            straight = 0
            if last != "" and char not in seen and alphabet.index(last) == alphabet.index(char):
                valid_dupes += 1
                seen += char
        last = char

    if valid_straight and valid_dupes > 1 and not confusing:
        score += 1
        if score == 2:
            for char in value:
                print(char, end="")
            break

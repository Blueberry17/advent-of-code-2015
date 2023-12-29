total = 0

for line in open("input.txt").read().split("\n"):
    vowel_count = 0
    vowels = "aeiou"
    double = naughty = False
    last = ""

    for char in line:
        if char in vowels:
            vowel_count += 1
        if len(last) > 0:
            if last == char:
                double = True
            elif (last+char) in ["ab", "cd", "pq", "xy"]:
                naughty = True
                break
            last = char
        else:
            last += char

    if double and not naughty and vowel_count > 2:
        total += 1

print(total)

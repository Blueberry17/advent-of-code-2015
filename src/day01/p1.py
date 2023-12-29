brackets = open("input.txt").read()
up = brackets.count("(")
print(up-(len(brackets)-up))

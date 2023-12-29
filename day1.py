brackets = open("day1info.txt").read()
up = brackets.count("(")
down = brackets.count(")")
print(up-down)

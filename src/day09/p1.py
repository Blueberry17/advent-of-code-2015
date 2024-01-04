import itertools

file = "input.txt"
graph = []
length = 8
for i in range(length):
	graph.append([0]*length)

names = {}
for line in open(file).read().split("\n"):
	new_names = [line.split()[0], line.split()[2]]
	for name in new_names:
		if name not in names:
			names[name] = len(names)

for line in open(file).read().split("\n"):
	line = line.split()
	to, fro, dist = names[line[0]], names[line[2]], int(line[4])
	graph[to][fro] = dist
	graph[fro][to] = dist

for i in graph:
	for j in i:
		print(f"{j}\t", end="")
	print()


min_dist = float("inf")
for i in itertools.permutations("01234567"):
	distance = 0
	last = i[0]
	for j in i[1:]:
		distance += graph[int(last)][int(j)]
		last = j
	if distance < min_dist:
		min_dist = distance

print(min_dist)

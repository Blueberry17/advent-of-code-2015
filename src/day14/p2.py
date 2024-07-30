speeds = open("input.txt").read().split("\n")

reindeer = []
for info in speeds:
    parts = info.split()
    # speed, duration, rest, fatigue, distance, stopped, points
    reindeer.append([int(parts[3]), int(parts[6]), int(parts[-2]), 0, 0, 0, 0])

time = 2503
sec = 0
while sec < time:
    distances = []
    for i in reindeer:
        if i[-2] == 0:
            i[4] += i[0]
            i[3] += 1
            if i[3] == i[1]:
                i[-2] = i[2]
                i[3] = 0
        else:
            i[-2] -= 1
        distances.append(i[4])

    furthest = 0
    max_indexes = []
    for index in range(len(distances)):
        if distances[index] > furthest:
            furthest = distances[index]
            max_indexes = [index]
        elif distances[index] == furthest:
            max_indexes.append(index)
    for index in max_indexes:
        reindeer[index][-1] += 1

    sec += 1

max_score = 0
for score in reindeer:
    if score[-1] > max_score:
        max_score = score[-1]
print(max_score)

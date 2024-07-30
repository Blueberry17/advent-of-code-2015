speeds = open("input.txt").read().split("\n")

furthest = 0
for info in speeds:
    parts = info.split()
    speed, duration, rest = int(parts[3]), int(parts[6]), int(parts[-2])
    fatigue = 0
    distance = 0
    time = 2503
    sec = 0
    while sec < time:
        distance += speed
        fatigue += 1
        if fatigue == duration:
            fatigue = 0
            sec += rest
        sec += 1
    if distance > furthest:
        furthest = distance
print(furthest)

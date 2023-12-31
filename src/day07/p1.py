wires = {}
lines = open("input.txt").read().split("\n")

while len(lines) > 0:
    new_lines = []
    for line in lines:
        parts = line.split()

        new_parts = []
        try:
            if "NOT" not in line and len(parts) != 3:
                for part in [parts[0], parts[2]]:
                    if part in wires:
                        new_parts.append(wires[part])
                    else:
                        new_parts.append(int(part))
                part1, part2 = new_parts

            elif len(parts) == 3:
                if parts[0] in wires:
                    part = wires[parts[0]]
                else:
                    part = int(parts[0])

            else:
                if parts[1] in wires:
                    part = wires[parts[1]]
                else:
                    part = int(parts[1])

        except ValueError:
            new_lines.append(line)
            continue

        if "AND" in line:
            wires[parts[-1]] = part1 & part2

        elif "OR" in line:
            wires[parts[-1]] = part1 | part2

        elif "NOT" in line:
            wires[parts[-1]] = ~part & 65535

        elif "LSHIFT" in line:
            wires[parts[-1]] = part1 << part2

        elif "RSHIFT" in line:
            wires[parts[-1]] = part1 >> part2

        else:
            wires[parts[-1]] = part

    lines = new_lines

print(wires["a"])

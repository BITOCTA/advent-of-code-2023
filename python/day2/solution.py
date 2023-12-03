from collections import defaultdict
from pathlib import Path


lines = None

### PART 1
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()

ids_sum = 0

limits = {"red": 12, "green": 13, "blue": 14}

for l in lines:
    l_split = l.split(":")
    game_id = int(l_split[0].split()[1])

    sets = l_split[1].split(";")

    possible = True

    for s in sets:
        cubes = s.split(",")
        for c in cubes:
            num, color = c.split()
            if int(num) > limits[color]:
                possible = False
                break
        if not possible:
            break
    if possible:
        ids_sum += game_id


print(ids_sum)


power_sum = 0

for l in lines:
    l_split = l.split(":")
    game_id = int(l_split[0].split()[1])

    sets = l_split[1].split(";")

    colors = defaultdict(int)

    for s in sets:
        cubes = s.split(",")
        for c in cubes:
            num, color = c.split()
            if int(num) > colors[color]:
                colors[color] = int(num)

    c1, c2, c3 = dict(colors).values()
    power_sum += c1 * c2 * c3

print(power_sum)

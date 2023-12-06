from pathlib import Path


lines = None

### PART 1
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()


times = list(map(int, (lines[0].split(":")[1].split())))
distances = list(map(int, (lines[1].split(":")[1].split())))


total_ways = 1
for i, t in enumerate(times):
    record_distance = distances[i]

    count = 0
    for hold_for in range(1, t):
        distance = hold_for * (t - hold_for)
        if distance > record_distance:
            count += 1
    print(count)
    total_ways *= count

print(total_ways)

times = [int("".join(list(map(str, times))))]
distances = [int("".join(list(map(str, distances))))]

total_ways = 1
for i, t in enumerate(times):
    record_distance = distances[i]

    count = 0
    for hold_for in range(1, t):
        distance = hold_for * (t - hold_for)
        if distance > record_distance:
            count += 1
    total_ways *= count

print(total_ways)

from collections import defaultdict
from pathlib import Path
from collections import deque


lines = None

### PART 1
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()

keys = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]


maps = defaultdict(lambda: [])


current_key = None

for l in lines[1:]:
    if len(l) == 0:
        continue
    if l[0].isdigit():
        dest, src, rng = map(int, l.split())
        maps[current_key].append((src, src + rng - 1, dest))
    else:
        for k in keys:
            if l.startswith(f"{k}-"):
                current_key = k
                break


seeds = lines[0].split(":")[1].split()

min_s_value = float("inf")

for s in seeds:
    s_value = int(s)
    for k in keys:
        for rng in maps[k]:
            if rng[0] <= s_value <= rng[1]:
                s_value = rng[2] + (s_value - rng[0])
                break
    if s_value < min_s_value:
        min_s_value = s_value


print(min_s_value)

paired_seeds = [
    (int(seeds[i]), int(seeds[i + 1]) + int(seeds[i])) for i in range(0, len(seeds), 2)
]

min_s_value = float("inf")


o_maps = {}


paired_seeds = deque(
    [
        (int(seeds[i]), int(seeds[i + 1]) + int(seeds[i]) - 1)
        for i in range(0, len(seeds), 2)
    ]
)


for i, k in enumerate(keys):
    new_ranges = []
    for pair in paired_seeds:
        found_matching = False
        for rng in maps[k]:
            if pair[1] < rng[0] or pair[0] > rng[1]:  # +  + |  |  or |  | + +
                continue
            else:
                found_matching = True
                start, end = max(pair[0], rng[0]), min(rng[1], pair[1])
                if (
                    pair[0] < rng[0] and pair[1] < rng[1] and i == len(keys) - 1
                ):  # + | + |
                    new_ranges.append((pair[0], rng[0] - 1))
                if (
                    pair[0] > rng[0] and pair[1] > rng[1] and i == len(keys) - 1
                ):  # | + | +
                    new_ranges.append((rng[1] + 1, pair[1]))
                if (
                    pair[0] < rng[0] and pair[1] > rng[1] and i == len(keys) - 1
                ):  # + |  | +
                    new_ranges.append((pair[0], rng[0] - 1))
                    new_ranges.append((rng[1] + 1, pair[1]))

                overlapping_range = (
                    rng[2] + (start - rng[0]),
                    ((rng[2] + (start - rng[0])) + (end - start)),
                )
                new_ranges.append(overlapping_range)

        if not found_matching:
            new_ranges.append(pair)
    paired_seeds = deque(new_ranges)

print(sorted(new_ranges, key=lambda x: x[0])[0][0])

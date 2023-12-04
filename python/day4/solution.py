from collections import defaultdict
from pathlib import Path


lines = None

### PART 1
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()

sum_points = 0

for l in lines:
    _, l_split = l.split(":")

    winning, ours = map(lambda s: set(s.split()), l_split.split("|"))

    inter = winning.intersection(ours)
    if len(inter) > 0:
        sum_points += 2 ** (len(winning.intersection(ours)) - 1)


print(sum_points)

### PART 2
copies = defaultdict(lambda: 1)

for l_i, l in enumerate(lines):
    _, l_split = l.split(":")

    winning, ours = map(lambda s: set(s.split()), l_split.split("|"))

    inter = winning.intersection(ours)
    if len(inter) > 0:
        for _ in range(copies[l_i]):
            winning_cards = len(inter)

            for w_c in range(1, winning_cards + 1):
                copies[l_i + w_c] += 1

copies_sum = 0
for i in range(len(lines)):
    copies_sum += copies[i]

print(copies_sum)
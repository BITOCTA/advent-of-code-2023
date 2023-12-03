import re
from pathlib import Path


lines = None

### PART 1
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()

sum_of_cal = 0

for l in lines:
    first_num = None
    last_num = None
    for c in l:
        try:
            num = int(c)
            if first_num is None:
                first_num = num
            last_num = num
        except ValueError:
            continue
    sum_of_cal += int(f"{first_num}{last_num}")

print(sum_of_cal)

## PART 2

sum_of_cal = 0

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

res_nums = []

for l in lines:
    num_word = ""
    first_num = None
    last_num = None
    for c in l:
        try:
            num = int(c)
            if first_num is None:
                first_num = num
            last_num = num
            num_word = ""
        except ValueError:
            num_word += c
            try:
                if len(num_word) >= 3:
                    for i, e in enumerate(nums):
                        re_search = re.search(e, num_word)
                        if re_search is not None:
                            if first_num is None:
                                first_num = i + 1
                            last_num = i + 1
                            num_word = num_word[num_word.index(e) + len(e) - 1 :]
            except ValueError:
                continue

    res_nums.append(f"{first_num}{last_num}\n")
    sum_of_cal += int(f"{first_num}{last_num}")


print(sum_of_cal)

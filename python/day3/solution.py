from pathlib import Path


lines = None

### PART 1
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()

part_numbers_sum = 0

line_length = len(lines[0])


not_symbols = {"."}
for i in range(0, 10):
    not_symbols.add(str(i))

filler = "." * line_length
lines = ["." * line_length, *lines, "." * line_length]

for i, l in enumerate(lines):
    lines[i] = [".", *l, "."]


for l_index, l in enumerate(lines):
    number = ""
    add_number = False
    for char_index, char in enumerate(l):
        try:
            digit = int(char)
            number += str(digit)
            symbols_arounds = set()
            if not add_number:
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        symbols_arounds.add(lines[l_index + y][char_index + x])
            if len(symbols_arounds.difference(not_symbols)) != 0:
                add_number = True
        except ValueError:
            if add_number:
                part_numbers_sum += int(number)
                add_number = False
            number = ""

            continue

print(part_numbers_sum)


### PART 2

ratios_sum = 0

for l_index, l in enumerate(lines):
    for char_index, char in enumerate(l):
        if char == "*":
            rows = []
            numbers = set()

            for y in [-1, 0, 1]:
                lines_cut = lines[l_index + y][char_index - 3 : char_index + 4]
                if (
                    not lines_cut[2].isdigit()
                    and not lines_cut[3].isdigit()
                    and not lines_cut[4].isdigit()
                ):
                    continue
                else:
                    for ind in [2, 3, 4]:
                        if lines_cut[ind].isdigit():
                            number = lines_cut[ind]

                            no_left = False
                            no_right = False

                            for i in range(1, 3):
                                if not no_left and lines_cut[ind - i].isdigit():
                                    number = f"{lines_cut[ind-i]}{number}"
                                else:
                                    no_left = True
                                if not no_right and lines_cut[ind + i].isdigit():
                                    number = f"{number}{lines_cut[ind+i]}"
                                else:
                                    no_right = True
                                if no_left and no_right:
                                    break
                            numbers.add(number)
            numbers = list(numbers)

            if len(numbers) == 2:
                ratios_sum += int(numbers[0]) * int(numbers[1])

print(ratios_sum)

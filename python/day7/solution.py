from pathlib import Path

from functools import cmp_to_key
import re
from collections import Counter


lines = None

### PART 1 (delete joker logic for part 1)
with open(Path(__file__).resolve().parent / "input.txt", "r+") as f:
    cont = f.read()
    lines = cont.splitlines()


def classify_hand(hand):
    counts = Counter(hand)
    unique_cards = len(counts)

    if "J" in counts:
        to_replace = counts.most_common(1)[0][0]
        if to_replace == "J" and len(counts) != 1:
            hand_modified = hand.replace("J", counts.most_common(2)[1][0])
        else:
            hand_modified = hand.replace("J", to_replace)
        counts = Counter(hand_modified)
        unique_cards = len(counts)

    if unique_cards == 1:
        return 7
    elif unique_cards == 2:
        if 4 in counts.values():
            return 6
        else:
            return 5
    elif unique_cards == 3:
        if 3 in counts.values():
            return 4
        else:
            return 3
    elif unique_cards == 4:
        return 2
    else:
        return 1


def compare_hands(hand1, hand2):
    type1 = classify_hand(hand1[0])
    type2 = classify_hand(hand2[0])

    if type1 != type2:
        return type1 - type2

    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 1,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    for card1, card2 in zip(hand1[0], hand2[0]):
        if card_values[card1] != card_values[card2]:
            return card_values[card1] - card_values[card2]

    return 0


compare_key = cmp_to_key(compare_hands)

lines = list(map(lambda x: x.split(), lines))

hands_len = len(lines)

print(
    sum(
        map(
            lambda x: (hands_len - x[0]) * int(x[1][1]),
            enumerate(sorted(lines, key=compare_key, reverse=True)),
        )
    )
)

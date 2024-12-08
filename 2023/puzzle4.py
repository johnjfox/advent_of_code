import re
import numpy as np


def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()

    # drop the end of line
    lines_data = [l[:-1] for l in raw]

    # parse the lines
    num_winners = list()

    for l in lines_data:
        s = str.split(l, ":")
        game = str.split(s[1], "|")
        winners = [int(n) for n in re.findall(r"\d+", game[0])]
        mine = [int(n) for n in re.findall(r"\d+", game[1])]
        num = 0
        for m in mine:
            if m in winners:
                num = num + 1
        num_winners.append(num)
    return num_winners


def rec_count(cnt_by_card):
    if len(cnt_by_card) == 0:
        return 0
    else:
        return cnt_by_card
        card = cnt_by_card.pop()
        cnt = cnt_by_card[card]
        return cnt + rec_count(cnt_by_card)


num_winners = get_data("puzzle4")
print(num_winners)
print("-------")

num_cards = [1] * len(num_winners)

print(num_cards)

for i in range(0, len(num_winners)):
    for j in range(0, num_winners[i]):
        num_cards[i + j + 1] = num_cards[i + j + 1] + num_cards[i]
    print(i + 1, num_cards)

result = 0
for i in range(0, len(num_cards)):
    result += num_cards[i]

print(result)

test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

from collections import defaultdict

translate_card = {
    "A": "C",
    "K": "B",
    "Q": "A",
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


def translate(hand: str) -> str:
    return "".join([str(translate_card[c]) for c in hand])


def score_hand(hand: str) -> int:
    v = int(translate(hand), 16)
    cnt_by_c = defaultdict(lambda: 0)
    for c in hand:
        cnt_by_c[c] += 1
    s = list(cnt_by_c.values())
    s.sort(reverse=True)
    if s[0] == 5:
        val = 6e6
    elif s[0] == 4:
        val = 5e6
    elif s[0] == 3:
        if s[1] == 2:
            val = 4e6
        else:
            val = 3e6
    elif s[0] == 2:
        if s[1] == 2:
            val = 2e6
        else:
            val = 1e6
    else:
        val = 0
    return val + v


def compare(item1, item2):
    if item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    else:
        return 0


score_hand("32T3K")

fname = "data/" + "puzzle" + ".txt"
print(f"---- READING DATA FROM {fname}")
~~` with open(fname) as f:
    raw = f.readlines()

# drop the end of line
lines_data = [l[:-1] for l in raw]

lines_data = test.splitlines()
d = [str.split(l, " ") for l in lines_data]
scores = [(score_hand(l[0]), int(l[1])) for l in d]
scores.sort(key=lambda x: x[0], reverse=True)
result = 0
for i in range(len(scores)):
    result += scores[i][1] * (i + 1)

print(result)

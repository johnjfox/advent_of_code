import re
import numpy as np
from collections import defaultdict

filename = "puzzle2"

RED = 12
GREEN = 13
BLUE = 14


def check_round(round):
    return (round["red"] <= RED) & (round["green"] <= GREEN) & (round["blue"] <= BLUE)


def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()

    # drop the end of line
    lines_data = [l[:-1] for l in raw]

    # parse the lines
    result = 0
    total = 0
    for l in lines_data:
        round = defaultdict(lambda: 0)
        s = str.split(l, ":")
        id_str = int(re.findall(r"\d+", s[0])[0])
        rhs = s[1]
        chk = True
        for r in str.split(rhs, ";"):
            for p in str.split(r, ","):
                v, k = str.split(str.strip(p), " ")
                round[k] = max(round[k], int(v))
            # chk = chk & check_round(round)
        pwr = round["red"] * round["green"] * round["blue"]
        print(id_str, round, pwr)
        if chk:
            result += pwr
    return result


print(get_data("puzzle2"))

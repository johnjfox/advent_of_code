from collections import defaultdict
import re
import numpy as np

filename = "puzzle7"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()
    tmp = [sub[:-1].split(':') for sub in raw]
    data = [[int(sub[0])] + list(map(int, sub[1].split())) for sub in tmp]
    return data


def equation(soln, terms, tmp):
    if len(terms) == 0:
        return soln == tmp
    return (equation(soln, terms[1:], int(tmp) + int(terms[0])) or
            equation(soln, terms[1:], int(tmp) * int(terms[0])) or
            equation(soln, terms[1:], int(str(tmp) + str(terms[0]))))

def solve1(data):
    data = get_data(filename)
    result = [equation(int(d[0]), d[2:], d[1]) for d in data]
    soln = 0
    for i, r in enumerate(result):
        if r:
            soln += data[i][0]

    return result


print(solve1(filename))

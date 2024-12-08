from collections import defaultdict
import re
import numpy as np

filename = "puzzle8"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()
    data = [list(l[:-1]) for l in raw]
    return data


def find_antenna(data):
    antenna = defaultdict(list)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != ".":
                antenna[data[i][j]].append((i, j))
    return antenna


def on_map(cand, nrow, ncol):
    return cand[0] >= 0 and cand[0] < nrow and cand[1] >= 0 and cand[1] < ncol

def solve1(data):
    data = get_data(filename)
    antenna = find_antenna(data)
    nrow = len(data)
    ncol = len(data[0])
    result = []
    for k,v in antenna.items():
        for i in range(len(v)-1):
            for j in range(i+1, len(v)):
                cand1 = (2*v[i][0] - v[j][0], 2*v[i][1] - v[j][1])
                if on_map(cand1, nrow, ncol):
                    result.append(cand1)
                cand2 = (2*v[j][0] - v[i][0], 2*v[j][1] - v[i][1])
                if on_map(cand2, nrow, ncol):
                    result.append(cand2)
                pass
    nloc = len(set(result))

    return nloc


def solve1a(data):
    data = get_data(filename)
    antenna = find_antenna(data)
    nrow = len(data)
    ncol = len(data[0])
    result = []
    for k,v in antenna.items():
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                dr = v[i][0] - v[j][0]
                dc = v[i][1] - v[j][1]
                niter = min(int((nrow-i)/ abs(dr)), int((ncol-j) / abs(dc)))
                for k in range(niter):
                    cand1 = (v[i][0] + k*dr, v[i][1] + k*dc)
                    if on_map(cand1, nrow, ncol):
                        result.append(cand1)
                    cand2 = (v[j][0] - dr, v[j][1] - dc)
                    if on_map(cand2, nrow, ncol):
                        result.append(cand2)

    nloc = len(set(result))

    return nloc

print(solve1a(filename))

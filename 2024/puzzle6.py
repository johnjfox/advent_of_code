from collections import defaultdict
import re
import numpy as np

filename = "puzzle6"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()
    data_list = [list(sub[:-1]) for sub in raw]
    data = np.array(data_list)
    return data

def init_state(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j] == '^'):
                return (i, j), 'U'

def boundary(state, nrow, ncol):
    if (state[0] == 0 or state[0] == nrow - 1 or state[1] == 0 or state[1] == ncol - 1):
        return True
    return False


def lookahead(state, dir, data):
    i, j = state
    if (dir == 'U'):
        next= (i-1, j)
    if (dir == 'D'):
        next = (i+1, j)
    if (dir == 'L'):
        next = (i, j-1)
    if (dir == 'R'):
        next = (i, j+1)
    return next, data[next[0], next[1]]


def move(state, dir, next_state, next_cell, data, turns):
    if (next_cell == '#'):
        turns[state[0], state[1]] = dir
        if (dir == 'U'):
            dir = 'R'
        elif (dir == 'R'):
            dir = 'D'
        elif (dir == 'D'):
            dir = 'L'
        elif (dir == 'L'):
            dir = 'U'
    else:
        data[state[0], state[1]] = dir
        state = next_state
    return state, dir, data, turns


def eval(data):
    cnt = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                cnt = cnt + 1
    # add in the final square
    return cnt + 1

def solve1(data):
    data = get_data(filename)
    # data = np.pad(data, 3, mode='constant', constant_values='0')
    state0, dir0 = init_state(data)
    nrow = len(data)
    ncol = len(data[0])
    results = 0
    for i in range(nrow):
        for j in range(ncol):
            if i == 10 and j == 13:
                continue
            print(i,j)
            if (data[i,j] == '#' and state[0] != i and state[1] != j):
                continue
            cand = data.copy()
            cand[i,j] = '#'
            turns = np.full((nrow, ncol), '.', dtype='U1')
            state = state0
            dir = dir0
            while not boundary(state, nrow, ncol):
                next_state, next_cell = lookahead(state, dir, cand)
                if next_cell == dir:
                    results = results+1
                    break
                state, dir, cand, turns = move(state, dir, next_state, next_cell, cand, turns)

    # result = eval(data)
    return results


print(solve1(filename))

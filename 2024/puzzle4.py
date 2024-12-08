from collections import defaultdict
import re
import numpy as np

filename = "puzzle4"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()
    data = [list(sub[:-1]) for sub in raw]
    return data


def solve1(data):
    data = get_data(filename)
    cnt = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (j <= len(data[i]) - 4) and ''.join(data[i][j:j+4]) == 'XMAS':
                cnt = cnt + 1
                print(i,j,'HOR')
            if (j <= len(data[i]) - 4) and ''.join(data[i][j:j+4]) == 'SAMX':
                cnt = cnt + 1
                print(i, j, 'HOR REV')
            if (i <= len(data) - 4) and ''.join([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]) == 'XMAS':
                cnt = cnt + 1
                print(i, j, 'VER')
            if (i <= len(data) - 4) and ''.join([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]) == 'SAMX':
                cnt = cnt + 1
                print(i, j, 'VER REV')
            if (j <= len(data[i]) - 4) and (i <= len(data) -4) and ''.join([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]]) == 'XMAS':
                cnt = cnt + 1
                print(i, j, 'DIAG')
            if (j >= 3) and (i <= len(data) -4) and ''.join([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]]) == 'XMAS':
                cnt = cnt + 1
                print(i, j, 'ANTIDIAG')
            if (j <= len(data[i]) - 4) and (i <= len(data) -4) and ''.join([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]]) == 'SAMX':
                cnt = cnt + 1
                print(i, j, 'DIAG REV')
            if (j >= 3) and (i <= len(data) -4) and ''.join([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]]) == 'SAMX':
                cnt = cnt + 1
                print(i, j, 'ANTI DIAG REV')
            pass
    return cnt


def solve1a(data):
    data = get_data(filename)
    cnt = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 'X' and data[i][j] != 'S':
                continue

            if j <= len(data[i]) - 4:
                test = ''.join(data[i][j:j+4])
                if test == 'XMAS' or test == 'SAMX':
                    cnt = cnt + 1

            if i <= len(data) - 4:
                test = ''.join([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]])
                if test == 'XMAS' or test == 'SAMX':
                    cnt = cnt + 1

            if (j <= len(data[i]) - 4) and (i <= len(data) -4):
                test =  ''.join([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]])
                if test == 'XMAS' or test == 'SAMX':
                    cnt = cnt + 1

            if (j >= 3) and (i <= len(data) -4):
                test = ''.join([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]])
                if test == 'XMAS' or test == 'SAMX':
                    cnt = cnt + 1
            pass
    return cnt


def logic(s):
    return int(s == 'XMAS' or s == 'SAMX')

def solve1b(data):
    data = np.array(get_data(filename))
    data = np.pad(data, 3, mode='constant', constant_values='0')
    cnt = 0
    for i in range(3, len(data)-3):
        for j in range(3,len(data[i])-3):
            if data[i][j] != 'X' and data[i][j] != 'S':
                continue
            cnt = cnt + logic(''.join(data[i][j:j+4]))
            cnt = cnt + logic(''.join([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]))
            cnt = cnt + logic(''.join([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]]))
            cnt = cnt + logic(''.join([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]]))

    return cnt


def solve2(data):
    data = get_data(filename)
    cnt = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[i])-1):
            if data[i][j] != 'X' and data[i][j] != 'S':
                continue
            l2r = ''.join([data[i-1][j-1], data[i][j], data[i+1][j+1]])
            r2l = ''.join([data[i-1][j+1], data[i][j], data[i + 1][j-1]])
            cnt = cnt + ((l2r == 'MAS') or (l2r == 'SAM')) and ((r2l == 'MAS') or (r2l == 'SAM'))

    return cnt

print(solve1b(filename))

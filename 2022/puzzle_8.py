import time
import numpy as np

from collections import defaultdict
import numpy as np

with open('data/puzzle8.txt') as f:
    lines = f.readlines()


def test1(m, i, j, max_i, max_j):
    res  = ((i == 0) or
            (j == 0) or
            (i == max_i-1) or
            (j == max_j-1) or
            (m[i,j] > np.max(m[:i, j], initial=-1)) or
            (m[i,j] > np.max(m[i+1:, j], initial=-1)) or
            (m[i,j] > np.max(m[i   , :j], initial=-1)) or
            (m[i,j] > np.max(m[i   , j+1:], initial=-1)))
    # print(i, j, max_i, max_j, m[i,j], res)
    return res

def bracket(r, val):
    for ind, v in r:
        if val > v:
            break
    return (ind, ind+1)

def test2(map, i, j, max_i, max_j):
    left  = 0 if i==0     else 1 + np.min(np.where(np.flip(map[i,:j]) >= map[i,j]), initial=j-1)
    right = 0 if i==max_i else 1 + np.min(np.where(map[i,j+1:] >= map[i,j]), initial=max_j-j-2)
    up    = 0 if j==0     else 1 + np.min(np.where(np.flip(map[:i,j]) >= map[i,j]), initial=i-1)
    down  = 0 if j==max_j else 1 + np.min(np.where(map[i+1:,j] >= map[i,j]), initial=max_i-i-2)
    res = up*down*left*right
    print("----", up, down, left, right, "=", res)
    return res


data = [[int(t) for t in l.strip()] for l in lines]

map = np.array(data)
d = map.shape

# res_matrix = np.zeros(d)
# for i in range(d[0]):
#     for j in range(d[1]):
#         res_matrix[i,j] = test1(map, i, j, d[0], d[1])

res2_matrix = np.zeros(d)
for i in range(1, d[0]-1):
    for j in range(1, d[1]-1):
        res2_matrix[i,j] = test2(map, i, j, d[0], d[1])

# print(np.sum(res_matrix))

print(np.max(res2_matrix))

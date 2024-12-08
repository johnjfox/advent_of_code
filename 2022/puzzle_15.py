import numpy as np
import re

with open('data/puzzle15.txt') as f:
    lines = f.readlines()

rec = []
for l in lines:
    dig = re.findall(r'-*\d+', l)
    rec.append([int(d) for d in dig])
readings = np.array(rec)
# min_x = min(min(readings[:, 0]), min(readings[: , 2]))
# max_x = max(max(readings[:, 0]), max(readings[: , 2]))
# min_y = min(min(readings[:, 1]), min(readings[: , 3]))
# max_y = max(max(readings[:, 1]), max(readings[: , 1]))

# readings[:,0] = readings[:,0] - min_x
# readings[:,2] = readings[:,2] - min_x
# readings[:,1] = readings[:,1] - min_y
# readings[:,3] = readings[:,3] - min_y

# map = np.zeros((max_y - min_y+1, max_x - min_x+1))
map = {}

iter=0
for r in readings:
    iter += 1
    print(iter, '---', r)
    x0, y0, x1, y1 = r
    d = abs(x1-x0) + abs(y1-y0)
    for i in range(0,d+1):
        for j in range(0,d-i+1):
            map[(y0+i, x0-j)] = 1
            map[(y0-i, x0-j)] = 1
            map[(y0+i, x0+j)] = 1
            map[(y0-i, x0+j)] = 1
    # map[y0, x0] = 10000
    # print(1)

res = [k for k,_ in map.items() if k[0] == 2000000]
print(1)
#%%

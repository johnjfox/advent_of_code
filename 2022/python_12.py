import numpy as np

def reachable(map, y_orig, x_orig, y_dest, x_dest):
    if (y_dest < 0) or (y_dest >= map.shape[0]):
        return False
    if (x_dest < 0) or (x_dest >= map.shape[1]):
        return False
    orig = map[y_orig, x_orig]
    orig = 'a' if orig == 'S' else orig
    dest = map[y_dest, x_dest]
    dest = 'z' if dest == 'E' else dest
    res = (ord(orig) == ord(dest) - 1) or (ord(orig) >= ord(dest))
    return res

with open('data/puzzle12.txt') as f:
    lines = f.readlines()

data = [[t for t in l.strip()] for l in lines]

map = np.array(data)
# y_s, x_s = np.where(map == 'S')
y_e, x_e = np.where(map == 'E')

optimal = 100000000000
dims = map.shape
starts = np.where(map == 'a')

for i in range(len(starts[0])):
    y_s = starts[0][i]
    x_s = starts[1][i]
    # print(i, y_s, x_s)
    if (abs(y_s - y_e) + abs(x_s - x_e)) > optimal:
        break

    dist = 100000000 * np.ones(dims)
    dist[(y_s, x_s)] = 0
    queue = [(y_s, x_s)]
    while (len(queue) > 0):
        y, x = queue.pop(0)
        if y < 0 or y >= dims[0]: break
        if x < 0 or x >= dims[1]: break

        # if dist[y,x] > 0: break

        if reachable(map, y, x, y+1, x):
            if dist[y+1, x] > 100000: queue.append((y+1, x))
            dist[y+1,x] = min(dist[y,x]+1, dist[y+1,x])
        if reachable(map, y, x, y-1, x):
            if dist[y-1, x] > 100000: queue.append((y-1, x))
            dist[y-1,x] = min(dist[y,x]+1, dist[y-1,x])
        if reachable(map, y, x, y, x+1):
            if dist[y, x+1] > 100000: queue.append((y, x+1))
            dist[y,x+1] = min(dist[y,x]+1, dist[y,x+1])
        if reachable(map, y, x, y, x-1):
            if dist[y, x-1] > 100000: queue.append((y, x-1))
            dist[y,x-1] = min(dist[y,x]+1, dist[y,x-1])

    if dist[y_e, x_e] < optimal:
        optimal = dist[y_e, x_e]
        print(i, y_s, x_s, optimal)

print(optimal)
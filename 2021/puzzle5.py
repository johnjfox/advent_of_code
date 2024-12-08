import numpy as np


def sgn(x0,x1):
    return 1 if x1 > x0 else -1 if x1 < x0 else 0


class Line:

    def __init__(self, x0, y0, x1, y1):
        self.nPoints = 0
        self.points = list()
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        self.vertical = x0 == x1
        self.horizontal = y0 == y1
        self.include = self.vertical | self.horizontal

        nsteps = max(abs(x1-x0), abs(y1-y0))
        dx = sgn(x0, x1)
        dy = sgn(y0, y1)
        x = x0
        y = y0
        for i in range(nsteps+1):
            self.nPoints += 1
            self.points.append((x, y))
            x += dx
            y += dy
        return

class Board:
    minX = 10000
    maxX = -10000
    minY = 10000
    maxY = -10000

    def find_extremes(self, lines):
        for l in lines:
            self.maxX = max(self.maxX, l.x0)
            self.maxX = max(self.maxX, l.x1)
            self.maxY = max(self.maxY, l.y0)
            self.maxY = max(self.maxY, l.y1)
        self.minX = 0
        self.minY = 0
        return

    def __init__(self, lines: Line):
        self.find_extremes(lines)
        self.data = np.zeros((self.maxY+1, self.maxX+1))
        for l in lines:
            for p in l.points:
                self.data[p[1], p[0]] += 1
        return

    def num_intersections(self):
        nr, nc = self.data.shape
        cnt = 0
        for r in range(nr):
            for c in range(nc):
               if self.data[r,c] > 1:
                   cnt += 1
        return cnt

    def get_data(self):
        return self.data


def get_data(filename):
    fname = 'data/'+ filename + '.txt'
    print(f'---- READING DATA FROM {fname}')
    with open(fname) as f:
        raw = f.readlines()

    # drop the end of line
    lines_data = [l[:-1] for l in raw]

    # parse the lines
    lines = []
    for l in lines_data:
        pt_str = l.split(' -> ')
        pts_list= [pt.split(',') for pt in pt_str]
        pts = [int(j) for i in pts_list for j in i]
        # print(pt_str, pts)
        lines.append(Line(pts[0], pts[1], pts[2], pts[3]))

    return lines


lines = get_data('puzzle5')

board = Board(lines)

print(board.num_intersections())
#%%

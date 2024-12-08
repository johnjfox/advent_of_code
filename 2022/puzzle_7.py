import time
from collections import defaultdict

with open('data/test7.txt') as f:
    lines = f.readlines()

class Node():
    def __init__(self, name='', parent=None, size=0, children=[]):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size

    def getsize(self):
        childsize = sum([d.getsize() for d in self.children])
        return self.size + childsize

    def add(self, node):
        node.parent = self
        self.children.append(node)

    def print_tree(self, level=''):
        print(level, self.name, len(self.children), self.getsize())
        for k in self.children:
            k.print_tree(level+'-')
        return

def process(l):
    match l[1]:
        case 'cd':
            if l[2] == '..':
                return current_dir.parent
            else:
                return directory[l[2]]
        case 'ls':
            return current_dir
        case _:
            print("UNKNOWN")

directory = defaultdict(Node)
directory['/'] = Node('/', None, 0, [])
current_dir = directory['/']

# build the tree
for i in range(len(lines)):
    t = [tok for tok in lines[i].split()]

    match t[0]:
        case '$':
            current_dir = process(t)
        case 'dir':
            directory[t[1]] = Node(t[1], current_dir, 0, [])  # numeric
            current_dir.add(directory[t[1]])
        case _:
            directory[t[1]] = Node(t[1], current_dir, int(t[0]), [])  # numeric
            current_dir.add(directory[t[1]])

res = 0
for k,v in directory.items():
    s = v.getsize()
    # print(k,s)
    if (len(v.children) > 0) & (s < 100000):
        res += s

# directory['/'].print_tree()

print('RESULT 1: ', res)

#%%

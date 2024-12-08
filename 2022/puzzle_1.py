import numpy as np

class Elf:
    def __init__(self, c):
        self.calories = c
        self.total = sum(c)

def get_data(filename):
    fname = 'data/'+ filename + '.txt'
    print(f'---- READING DATA FROM {fname}')
    with open(fname) as f:
        raw = f.readlines()

    # drop the end of line
    lines_data = [l[:-1] for l in raw]

    # parse the lines
    elves = []
    food = []
    for l in lines_data:
        if (l == ''):
            elves.append(Elf(food))
            food = []
        else:
            item = int(l.strip())
            # print(item)
            food.append(item)

    #  catch the last elf
    elves.append(Elf(food))
    return elves

elves = get_data('puzzle1')

max_to_date = -100000
for e in elves:
    if e.total > max_to_date:
        max_to_date = e.total

elf_list = [e.total for e in elves]
elf_list.sort(reverse=True)
print(elf_list[0])
print(sum(elf_list[0:3]))


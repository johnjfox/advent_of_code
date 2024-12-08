#---------------------------
filename ='puzzle3'
fname = 'data/'+ filename + '.txt'
print(f'---- READING DATA FROM {fname}')
with open(fname) as f:
    raw = f.readlines()
data = [r.strip() for r in raw]

#--------------------------- Part 1
def value(c):
    v = ord(c)
    return v-96 if v >= 97 else v-38


res = []
for d in data:
    l = len(d)
    for c in d[:int(l/2)]:
        if c in d[int(l/2):]:
            res.append(value(c))
            break
print('PART 1:', sum(res))

#--------------------------- Part 2
def intersection(lst1, lst2, lst3):
    t   = [v for v in lst1 if v in lst2]
    res = [v for v in t if v in lst3]
    return value(res[0])

res = []
i = 0
while (i < len(data)):
    res.append(intersection(data[i], data[i+1], data[i+2]))
    i += 3
print('PART 2:', sum(res))

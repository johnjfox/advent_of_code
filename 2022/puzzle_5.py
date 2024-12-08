import re as re
with open('data/puzzle5.txt') as f:
    data1, data2 = f.read().split('\n\n')

# temp = []
# for d in data1:
#     if d.find('[') != -1:
#         d2 = d.replace("    ", '[b] ')
#         t = re.findall('\[[bA-Z]\]*', d2)
#         temp.append([t1.strip().replace('[','').replace(']', '') for t1 in t])
#     else:
#         ncols = int(d.split()[-1])
# temp = [t for t in temp if len(t) > 0]
# temp.reverse()
#
# cols = [[] for i in range(ncols)]
# for v in temp:
#     for i in range(len(v)):
#         if v[i] != 'b': cols[i].append(v[i])
#         # print(i, v[i], '--', cols)


moves = data2.split('\n')

for m in moves:
    if len(m) > 0:
        _,cnt,_,start,_,tgt= m.split(' ')
    # cols[tgt] = cols[tgt] + list(cols[start][-cnt:])
    # cols[start] = cols[start][:(len(cols[start]) - cnt)]

res1 = [c[-1] for c in cols]
print(''.join(res1))

#%%

with open('data/puzzle4.txt') as f:
    raw = f.readlines()
data = [r.strip() for r in raw]

result1 = 0
result2 = 0
for d in data:
    t = [[int(y) for y in x.split('-')] for x in d.split(',')]
    result1 += (t[0][0] <= t[1][0] <= t[1][1] <= t[0][1]) | (t[1][0] <= t[0][0] <= t[0][1] <= t[1][1])
    result2 += len(range(max(t[0][0],t[1][0]), min(t[0][1], t[1][1])+1)) > 0

print('PART 1:', result1)
print('PART 2:', result2)

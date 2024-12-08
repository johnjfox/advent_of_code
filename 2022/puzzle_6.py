import time

with open('data/puzzle6.txt') as f:
    raw = f.read()
d = raw.strip()
current_time = time.time()
res1 = res2 = True
for i in range(0,len(d)):
    if (res1 & (len(set(d[i:i+4])) == 4)):
        print('PART 1:', i+4)
        res1 = False
    if (res2 & (len(set(d[i:i+14])) == 14)):
        print('PART 2:', i + 14)
        res2 = False
        break

# print('ANS 1= ',[i for i in range(0,len(d)-4) if len(set(d[i:i+4])) == 4][0]+4)
# print('ANS 2= ',[i for i in range(0,len(d)-14) if len(set(d[i:i+14])) == 14][0]+14)
print(1)

print(time.time() - current_time)

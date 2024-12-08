import time
import numpy as np
import pandas as pd

from collections import defaultdict
import numpy as np

# cpu = pd.read_csv('data/simple10.txt')
# cpu[['command', 'arg']] = cpu['instructions'].str.split(' ', n=1, expand=True)
# cpu['delta'] = cpu['arg'].fillna('0').astype(int).shift(1, fill_value=0)
# cpu['value'] = cpu['delta'].cumsum() + 1
#
# # for i in range(cpu.shape[0]):
#
# res_vec = cpu.iloc[19::40]['value']
# res = sum(res_vec)
# print(res)

with open('data/puzzle10.txt') as f:
    lines = f.readlines()

res = [1]
val = 1
for l in lines:
    tok = l.strip().split()
    match tok[0]:
        case 'noop':
            res.append(val)
        case 'addx':
            res.append(val)
            val += int(tok[1])
            res.append(val)

result = [i * res[i-1] for i in range(20, len(res), 40)]
print(sum(result))


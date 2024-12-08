import re
import numpy as np
from collections import defaultdict


# time_test = [7, 15, 30]
# distance_test = [9, 40, 200]

# time_test = [71530]
# distance_test = [940200]

# time_test = [47, 98, 66, 98]
# distance_test = [400, 1213, 1011, 1540]

time_test = [47986698]
distance_test = [400121310111540]


def distance(thold, tmax):
    return thold * (tmax - thold)


soln = list()

for i in range(len(time_test)):
    t = time_test[i]
    d = distance_test[i]

    rnd = [thold for thold in range(t) if distance(thold, t) > d]
    soln.append(len(rnd))

    pass

print(soln, "->", np.prod(soln))

from collections import defaultdict

filename = "test2"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()

    # drop the end of line
    nums = [l[:-1].split() for l in raw]

    # convert eacj elements in  nums to int
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            nums[i][j] = int(nums[i][j])
    return nums


def solve(filename):
    l0, l1  = get_data(filename)
    l0 = sorted(l0)
    l1 = sorted(l1)
    dict0 = defaultdict(int)
    dict1 = defaultdict(int)

    for i in range(len(l1)):
        dict1[int(l1[i])] += 1

    total = 0
    for i in range(len(l0)):
        total = total + int(l0[i]) * dict1[int(l0[i])]
    return total


print(solve("puzzle1"))
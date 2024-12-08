from collections import defaultdict

filename = "puzzle2"
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


def solve1(filename):
    l0 = get_data(filename)
    total = 0
    for i in range(len(l0)):
        delta = [l0[i][j + 1] - l0[i][j] for j in range(len(l0[i]) - 1)]
        abs_delta = [abs(x) for x in delta]
        sgn = [1 if x > 0 else -1 if x < 0 else 0 for x in delta]
        if max(abs_delta) <= 3 and ( all([x == 1 for x in sgn]) >= 1 or all([x == -1 for x in sgn])):
            total = total + 1
    return total


# print(solve1(filename))


def sub_soln(l0):
    delta1 = [l0[j + 1] - l0[j] for j in range(len(l0) - 1)]
    abs_delta = [abs(x) <= 3 for x in delta1]
    sgn = [1 if x > 0 else -1 if x < 0 else 0 for x in delta1]
    up = [x == 1 for x in sgn]
    down = [x == -1 for x in sgn]
    result = all(abs_delta) and (all(up) or all(down))
    return(result)


def solve2(filename):
    l0 = get_data(filename)
    total = 0
    for i in range(len(l0)):
        if sub_soln(l0[i]):
            total = total + 1
        else:
            for j in range(len(l0[i])):
                tmp = l0[i].copy()
                tmp.pop(j)
                if sub_soln(tmp):
                    total = total + 1
                    break
    return total

print(solve2(filename))
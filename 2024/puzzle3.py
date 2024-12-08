from collections import defaultdict
import re

filename = "puzzle3"

# filter_pattern = "don't\(\).*?do\(\)"
filter_pattern = "do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)"
# filter_pattern = "don't\(\)"
mul_pattern = "mul\([0-9]+,[0-9]+\)"
num_pattern = "[0-9]+"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        # raw = f.readlines()
        data = 'do()' + f.read() + 'don\'t()'
    return data


def solve(data):
    data = get_data(filename)
    process = False
    res = 0
    cmd_list = re.findall(filter_pattern, data)
    for cmd in cmd_list:
        match cmd:
            case "do()":
                process = True
            case "don't()":
                process = False
            case _:
                if process:
                    nums = re.findall(num_pattern, cmd)
                    res = res + int(nums[0]) * int(nums[1])
    return res


print(solve(filename))

import re

filename = "puzzle1"


def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()

    # drop the end of line
    lines_data = [l[:-1] for l in raw]

    convert = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        # "zero": "0",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    # convert a dict which maps the names of single digit integers into their values

    # parse the lines
    cum = list()
    total = 0
    for l in lines_data:
        # find the first digit in string l
        pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))"
        digits = re.findall(pattern, l)
        num = 10 * int(convert[digits[0]]) + int(convert[digits[-1]])
        total += num
        cum.append(num)
        print(l, digits, num, total)
    return total


print(get_data("puzzle1"))

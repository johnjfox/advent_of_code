from collections import defaultdict

filename = "puzzle5"

def get_data(filename):
    fname = "data/" + filename + ".txt"
    print(f"---- READING DATA FROM {fname}")
    with open(fname) as f:
        raw = f.readlines()

    # find the line that separates the two lists
    sep = raw.index("\n")

    # drop the end of line
    rules = [l[:-1].split('|') for l in raw[:sep]]
    pages = [l[:-1].split(',') for l in raw[sep+1:]]
    return rules, pages


def eval(l):
    return sum([int(g[int(len(g)/ 2)]) for g in l])


def organize(filename):
    raw_rules, pages = get_data(filename)

    # aggregate the rules into dicts
    rules = defaultdict(list)
    for r in raw_rules:
        rules[r[0]].append(r[1])

    # iterate thru the pages and determine which are ok
    good = []
    bad = []
    for p in pages:
        valid = True
        for i in range(len(p)-1):
            if not set(p[i+1:]).issubset(rules[p[i]]):
                valid = False
                break
        if valid:
            good.append(p)
        else:
            bad.append(p)

    return good, bad, rules


# correct a single manual
def correct(rules, candidates, corrected):
    if len(candidates) == 0:
        return corrected

    for c in range(len(candidates)):
        others = candidates[:c] + candidates[c+1:]
        if set(others).issubset(set(rules[candidates[c]])):
            corrected.append(candidates[c])
            return correct(rules, others, corrected)


def correct_all(rules, manuals):
    corrected = []
    for m in manuals:
        corrected.append(correct(rules, m, []))
    return corrected

def solve(filename):
    good, bad, rules = organize(filename)
    corrected = correct_all(rules, bad)
    pt1_result = eval(good)
    pt2_result = eval(corrected)
    print('done')

print(solve(filename))
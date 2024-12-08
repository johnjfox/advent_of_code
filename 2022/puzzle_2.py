
def value(c):
    match(c):
        case 'A' | 'X': return 1    # Rock
        case 'B' | 'Y': return 2    # Paper
        case 'C' | 'Z': return 3    # Scissors

def lose_score(c):
    return (value(c) + 1) % 3 + 1

def win_score(c):
    return (value(c) % 3) + 1

def score_round(r):
    # print(r)
    other = value(r[0])
    me = value(r[1])
    return me + 3*(me == other) + 6*(me == (other % 3 + 1))

def score_round2(r):
    match(r[1]):
        case 'X': return lose_score(r[0])
        case 'Y': return 3 + value(r[0])
        case 'Z': return 6 + win_score(r[0])

def get_data(filename):
    fname = 'data/'+ filename + '.txt'
    print(f'---- READING DATA FROM {fname}')
    with open(fname) as f:
        raw = f.readlines()

    rounds = [l.split() for l in raw]
    scores = [score_round(r) for r in rounds]
    return sum(scores)

print(get_data('puzzle2'))

#%%

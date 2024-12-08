def get_data(filename):
    with open('data/'+ filename + '_rolls.txt') as f:
        roll_str = f.readline()
    # print(roll_str)
    rolls = roll_str.split(',')
    with open('data/'+ filename + '.txt') as f:
        raw = f.readlines()
    board_str = [l[:-1] for l in raw]

    score=list()
    for l in board_str:
        if len(l) > 0:
            score.append(list(map(lambda v: int(v), l.split())))

    nplayers = int(len(score) / 5)
    lookup = dict()
    for i,row in enumerate(score):
        player = int(i/5)
        r = i % 5
        for c,v in enumerate(row):
            lookup.setdefault(str(v), []).append(((i,r,c)))
    return rolls, nplayers, lookup, score


def create_boards(nplayers, rolls, lookup):
    boards = []
    for i in range(5*nplayers):
        boards.append([0]*5)
    return boards


def check_rows(boards):
    # print(boards)
    for i,v in enumerate(boards):
        if sum(v) == 5:
            # print('++', v)
            return int(i/5)
    return -1


def check_cols(nplayers, boards):
    for i in range(5):
        for j in range(nplayers):
            for k in range(5):
                # print(i, j, k)
                s = boards[j*5+k][i]
                if s == 5:
                    # print('--', j)
                    return int(j/5)
    return -1


def check_winner(nplayers, boards):
    rw = check_rows(boards)
    if rw > 0:
        return rw
    rc = check_cols(nplayers, boards)
    if rc > 0:
        return rc
    return -1


def compute_board_val(w, nplayers, boards, score):
    s = 0
    # print(boards[5*w: 5*w+5])
    # print('===================')
    # print(score[5*w: 5*w+5])
    for r in score[5*w: 5*w+5]:
        s += sum(r)
    return s


def update_boards(nplayers, rolls, lookup, boards, score):
    for i, r in enumerate(rolls):
        update = lookup[r]
        for j, u in enumerate(update):
            boards[u[0]][u[2]] = 1
            score[u[0]][u[2]] = 0
            # print(i, r, j, u, u[0], u[2], boards[u[0]][u[2]], score[u[0]][u[2]])
        w = check_winner(nplayers, boards)
        if w > 0:
            res = compute_board_val(w, nplayers, boards, score) * int(r)
            print("WINNER:", w, res)
            break


rolls, nplayers, lookup, score = get_data('puzzle4')

boards = create_boards(nplayers, rolls, lookup)

score = update_boards(nplayers, rolls, lookup, boards, score)
#%%
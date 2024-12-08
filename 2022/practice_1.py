
def get_data(filename):
    fname = 'data/'+ filename + '.txt'
    print(f'---- READING DATA FROM {fname}')
    with open(fname) as f:
        raw = f.read().strip()

    cal_list_by_elf = raw.split("\n\n")
    total_cals_by_elf = [
        sum([int(cal) for cal in cal_list.split("\n")])
        for cal_list in cal_list_by_elf
    ]

    elves = raw.split('\n\n')
    rounds = [sum([int(cal) for cal in e.split('\n') ])
              for e in elves]
    return rounds.sort()

print(get_data('test1'))
#!/usr/bin/env python3

for hour_offset in range(0, 24, 6):

    train = open('data/train_b{:02}.csv'.format(hour_offset), 'w', newline='')
    test = open('data/test_b{:02}.csv'.format(hour_offset), 'w', newline='')
    data = open('data/data.txt')
    t = int(next(data))
    n, m = tuple(map(int, next(data).split()))

    for line_num, line in enumerate(data):
        hse = line_num // n # hours since epoch
        hod = hse % 24 # hour of day
        dse = (hse + hour_offset) // 24 # days since epoch
        dow = dse % 7 # day of week
        row = line_num % n
        for col, dem in enumerate(map(int, line.split())):
            out, lim = (test, -1) if dem == -1 else (train, None)
            out.write(','.join(map(str, (hse, row, col, hod, dow, dem)[:lim])) + '\n')

    data.close()
    train.close()
    test.close()

#!/usr/bin/env python3

train = open('data/train_a.csv', 'w', newline='')
test = open('data/test_a.csv', 'w', newline='')
data = open('data/data.txt')
t = int(next(data))
n, m = tuple(map(int, next(data).split()))

for line_num, line in enumerate(data):
    hse = line_num // n # hours since epoch
    hod = hse % 24 # hour of day
    row = line_num % n
    for col, dem in enumerate(map(int, line.split())):
        out, lim = (test, -1) if dem == -1 else (train, None)
        out.write(','.join(map(str, (hse, row, col, hod, dem)[:lim])) + '\n')

data.close()
train.close()
test.close()

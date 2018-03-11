#!/usr/bin/env python3

import numpy as np
from pandas import read_csv
from sklearn.ensemble import RandomForestRegressor

n_estimators = 1000
datasets_iters = [
    ('a', 16),
    ('b00', 4),
    ('b06', 4),
    ('b12', 4),
    ('b18', 4)
]

n_total_iters = sum(di[1] for di in datasets_iters)
n_test_samples = read_csv('data/test_{}.csv'.format(datasets_iters[0][0]), header=None).values.shape[0]
y_test_preds = np.ndarray(shape=(n_total_iters, n_test_samples), dtype=np.float64)

i = 0
for (dataset_name, n_iters) in datasets_iters:
    for dataset_iter in range(n_iters):
        print(dataset_name, dataset_iter + 1)
        dataframe_train = read_csv('data/train_{}.csv'.format(dataset_name), header=None)
        dataset_train = dataframe_train.values
        n_features = dataset_train.shape[1] - 1
        x_train = dataset_train[:, :n_features]
        y_train = dataset_train[:, n_features]
        dataframe_test = read_csv('data/test_{}.csv'.format(dataset_name), header=None)
        x_test = dataframe_test.values
        regr = RandomForestRegressor(n_estimators=n_estimators, n_jobs=-1)
        regr.fit(x_train, y_train)
        y_test_preds[i, :] = regr.predict(x_test)
        i += 1

y_test_pred = y_test_preds.mean(axis=0)
with open('results/result.csv', 'w', newline='') as result_file:
    result_file.write('id,demand\n')
    for x, y in zip(x_test, y_test_pred):
        result_file.write('{}:{}:{},{}\n'.format(*x[:3], y))

# -*- coding: utf-8 -*-
import graphlab as gl


def run(filepath, weights, reg, target):
    """
    Uses the different weights to recalculate recommendations
    using all of them
    """
    data = gl.SFrame.read_csv(filepath)
    cols = data.column_names()[2:-1]
    data['score'] = data.apply(
        lambda x: sum([weights[i] * x[cols[i]] for i in range(0, len(cols))]) + reg
    )

    for col in cols:
        del data[col]
    del data['label']

    data.save(target, format='csv')


if __name__ == '__main__':
    filepath = '/home/arthur/work/data/files/results/labeled/all.csv'
    base = '/home/arthur/work/data/files/results/'

    run(filepath, [-1.2651, 0.0, 0.502, 1.1044, 0.9727, -3.5864], 2.724, base + 'regression_6scores.csv')
    run(filepath, [-0.0932, 0.0, 0.45, 0.0315, 0.0398, -0.0272], 0.043, base + 'regression_5scores.csv')
    run(filepath, [-0.1206, -0.0226, 0.6082, 0.0879, 0.017, -0.1049], 0.0887, base + 'regression_4scores.csv')
    run(filepath, [-0.0766, -0.0485, 0.06342, 0.0, 0.0324, -0.0666], 0.1218, base + 'regression_3scores.csv')

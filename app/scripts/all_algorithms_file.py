# -*- coding: utf-8 -*-
import graphlab as gl


cf = gl.SFrame.read_csv('/home/arthur/work/data/files/results/labeled/cf_recs.csv', header=False)
sf = gl.SFrame.read_csv('/home/arthur/work/data/files/results/labeled/sf_recs.csv', header=False)
tnet = gl.SFrame.read_csv('/home/arthur/work/data/files/results/labeled/tnet_recs.csv', header=False)
trustsf = gl.SFrame.read_csv('/home/arthur/work/data/files/results/labeled/trustsf_recs.csv', header=False)
timecf1 = gl.SFrame.read_csv('/home/arthur/work/data/files/results/labeled/timesf_recs.csv', header=False)
timecf2 = gl.SFrame.read_csv('/home/arthur/work/data/files/results/labeled/timesf2_recs.csv', header=False)

res = cf.join(sf, ['X1', 'X2'], 'outer')
res = res.join(tnet, ['X1', 'X2'], 'outer')
res = res.join(trustsf, ['X1', 'X2'], 'outer')
res = res.join(timecf1, ['X1', 'X2'], 'outer')
res = res.join(timecf2, ['X1', 'X2'], 'outer')

res = res.fillna('X3', 0.0)
res = res.fillna('X3.1', 0.0)
res = res.fillna('X3.2', 0.0)
res = res.fillna('X3.3', 0.0)
res = res.fillna('X3.4', 0.0)
res = res.fillna('X3.5', 0.0)

res = res.fillna('X4', 0)
res = res.fillna('X4.1', 0)
res = res.fillna('X4.2', 0)
res = res.fillna('X4.3', 0)
res = res.fillna('X4.4', 0)
res = res.fillna('X4.5', 0)

res = res.pack_columns(['X4', 'X4.1', 'X4.2', 'X4.3', 'X4.4', 'X4.5'])

res['X9'] = res['X9'].apply(lambda x: 1 if sum(x) > 0 else 0)

# rename columns
res.rename({
    'X1': 'authorId',
    'X2': 'articleId',
    'X3': 'collaborativeFiltering',
    'X3.1': 'socialFiltering',
    'X3.2': 'trustNetwork',
    'X3.3': 'trustSF',
    'X3.4': 'time1SF',
    'X3.5': 'time2SF',
    'X9': 'label',
})

res.save('/home/arthur/work/data/files/results/labeled/all.csv', format='csv')
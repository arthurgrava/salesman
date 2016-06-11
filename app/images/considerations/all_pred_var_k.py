# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 7)]
x = k
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS', 'TRS']

# S@K
ucf = [5.49356,4.47554,4.62866,4.80905,4.96217,5.15305,]
tnet = [41.12604,44.0907,44.94854,45.42989,45.74087,45.8851,]
srs = [11.86255,10.10422,9.79672,9.70385,9.6667,9.66257,]
srs_ = [19.30051,18.31248,18.12449,18.05891,18.04361,18.04361,]
tsrs = [7.3657,4.23808,3.37916,2.98956,2.79789,2.66899,]
tsrs_ = [19.97705,18.96934,18.79775,18.68845,18.68517,18.67315,]
time = [12.40764,17.95827,17.982,18.0336,18.11202,17.99335,]
hsrs = []

plt.subplot(221)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.xlim((4, 31))
plt.xlabel('Vizinhos', fontsize=18)
plt.ylabel('S@10', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# MRR
ucf = [0.0223,0.01939,0.0202,0.02117,0.02193,0.02293,]
tnet = [0.16625,0.17596,0.17865,0.17953,0.17934,0.1792,]
srs = [0.04979,0.04265,0.04142,0.041,0.04093,0.04093,]
srs_ = [0.07967,0.07559,0.07506,0.07491,0.07488,0.07483,]
tsrs = [0.02882,0.01824,0.01553,0.01443,0.014,0.0135,]
tsrs_ = [0.08203,0.07834,0.07771,0.07743,0.07748,0.07737,]
time = [0.06737,0.07454,0.07468,0.07473,0.07498,0.07455,]
hsrs = []

plt.subplot(222)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.xlim((4, 31))
plt.xlabel('Vizinhos', fontsize=18)
plt.ylabel('MRR@10', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Recall
ucf = [0.00896,0.00757,0.00754,0.0077,0.00783,0.00793,]
tnet = [0.08233,0.08982,0.09187,0.09268,0.09317,0.09335,]
srs = [0.01783,0.01451,0.01403,0.01386,0.01378,0.01378,]
srs_ = [0.02964,0.02735,0.02699,0.02683,0.0268,0.0268,]
tsrs = [0.01041,0.0058,0.00491,0.00459,0.00444,0.00439,]
tsrs_ = [0.03039,0.02803,0.02769,0.02752,0.02752,0.02749,]
time = [0.01752,0.02684,0.02683,0.02685,0.02696,0.02682,]
hsrs = []

plt.subplot(223)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.xlim((4, 31))
plt.xlabel('Vizinhos', fontsize=18)
plt.ylabel('Recall@10', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Precision
ucf = [0.0009,0.00076,0.00075,0.00077,0.00078,0.00079,]
tnet = [0.00823,0.00898,0.00919,0.00927,0.00932,0.00934,]
srs = [0.00178,0.00145,0.0014,0.00139,0.00138,0.00138,]
srs_ = [0.00296,0.00274,0.0027,0.00268,0.00268,0.00268,]
tsrs = [0.00104,0.00058,0.00049,0.00046,0.00044,0.00044,]
tsrs_ = [0.00304,0.0028,0.00277,0.00275,0.00275,0.00275,]
time = [0.00175,0.00268,0.00268,0.00269,0.0027,0.00268,]
hsrs = []

plt.subplot(224)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.xlim((4, 31))
plt.xlabel('Vizinhos', fontsize=18)
plt.ylabel('Precision@10', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

plt.show()
#plt.savefig('/home/arthur/work/tese/images/all_k10_prediction.png', dpi=500)

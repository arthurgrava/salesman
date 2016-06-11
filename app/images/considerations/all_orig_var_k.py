# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 7)]
x = k
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS', 'TRS']

# S@K
ucf = [3.599,2.93235, 3.03268, 3.15087, 3.25119, 3.37626]
srs = [5.26641,4.4858,4.34928,4.30805,4.29156,4.28973]
srs_ = [8.08973,7.6756,7.59681,7.56932,7.56291,7.56291,]
tsrs = [7.02372,4.05105,3.23058,2.85814,2.67489,2.55166,]
tsrs_ = [8.3733,7.95093,7.879,7.83319,7.83182,7.82678,]
time = [9.38068,14.10149,14.08912,14.09782,14.09828,14.08316,]
tnet = [39.29195,42.15146,42.97239,43.43279,43.7301,43.86799,]
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
ucf = [0.0146, 0.01270, 0.01323,0.01387,0.01437,0.01502]
srs = [0.0221,0.01893,0.01839,0.0182,0.01817,0.01817,]
srs_ = [0.03339,0.03169,0.03146,0.0314,0.03138,0.03136,]
tsrs = [0.02748,0.01743,0.01485,0.0138,0.01339,0.01291,]
tsrs_ = [0.03438,0.03284,0.03257,0.03245,0.03247,0.03243,]
time = [0.05075,0.05699,0.05692,0.05693,0.05697,0.05691,]
tnet = [0.15883,0.16822,0.17079,0.17164,0.17145,0.17132,]
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
ucf = [0.0059,0.00496,0.00494,0.00504,0.00513,0.00519]
srs = [0.00792,0.00644,0.00623,0.00615,0.00612,0.00612,]
srs_ = [0.01242,0.01147,0.01131,0.01124,0.01123,0.01123,]
tsrs = [0.00992,0.00554,0.00469,0.00439,0.00425,0.0042,]
tsrs_ = [0.01274,0.01175,0.0116,0.01153,0.01153,0.01152,]
time = [0.01152,0.01754,0.01748,0.0175,0.01754,0.01747,]
tnet = [0.07866, 0.08587, 0.08783, 0.08861, 0.08907, 0.08925, ]
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
ucf = [0.00059,0.00050,0.00049,0.00050,0.00051,0.00052]
srs = [0.00079, 0.00064,0.00062, 0.00062,0.00061, 0.00061,]
srs_ = [0.00124, 0.00115,0.00113, 0.00112,0.00112, 0.00112,]
tsrs = [0.00099, 0.00055,0.00047, 0.00044,0.00042, 0.00042,]
tsrs_ = [0.00127,0.00117,0.00116,0.00115,0.00115,0.00115,]
time = [0.00115,0.00175,0.00175,0.00175,0.00175,0.00175,]
tnet = [0.00787,0.00859,0.00878,0.00886,0.00891,0.00892]
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
#plt.savefig('/home/arthur/work/tese/images/all_k10_original.png', dpi=500)

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

# plt.subplot(221)
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
plt.legend(legend, loc='best', fontsize=12)

#plt.show()
plt.savefig('/home/arthur/Dropbox/apresentacao_tese/images/detail_satk_original_var_k.png', dpi=500)

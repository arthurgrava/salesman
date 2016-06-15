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

# plt.show()
plt.savefig('/home/arthur/Dropbox/apresentacao_tese/images/detail_satk_prediction_var_k.png', dpi=500)

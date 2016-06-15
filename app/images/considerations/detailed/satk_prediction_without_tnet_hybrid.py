# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS']

# S@K
ucf = [3.637, 5.494, 6.714, 7.725, 8.652]
srs = [8.127, 11.863, 14.187, 15.806, 16.917]
srs_ = [13.088, 19.301, 23.195, 26.004, 28.146]
tsrs = [4.732, 7.366, 9.011, 10.154, 11.087]
tsrs_ = [13.613, 19.977, 23.984, 26.924, 29.077]
time = [12.388, 18.112, 21.687, 24.282, 26.251]

plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
plt.savefig('/home/arthur/Dropbox/apresentacao_tese/images/detail_satk_prediction_without_tnet_hybrid.png', dpi=500)

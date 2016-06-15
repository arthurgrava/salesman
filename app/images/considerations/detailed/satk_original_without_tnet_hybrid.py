# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS']

# S@K
ucf = [2.383, 3.599, 4.399, 5.062, 5.669]
srs = [3.608, 5.266, 6.299, 7.017, 7.51]
srs_ = [5.486, 8.09, 9.722, 10.899, 11.797]
tsrs = [4.512, 7.024, 8.592, 9.682, 10.572]
tsrs_ = [5.706, 8.373, 10.053, 11.285, 12.188]
time = [9.372, 14.098, 17.325, 19.717, 21.633]

plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize=12)

# plt.show()
plt.savefig('/home/arthur/Dropbox/apresentacao_tese/images/detail_satk_original_without_tnet_hybrid.png', dpi=500)

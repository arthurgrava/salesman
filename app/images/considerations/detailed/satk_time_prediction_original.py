# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k
legend = ['Time Train', 'Time Pred',]

# S@K
time = [9.372, 14.098, 17.325, 19.717, 21.633]
time2 = [12.388, 18.112, 21.687, 24.282, 26.251]

plt.plot(x, time, 'o--')
plt.plot(x, time2, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize=14)

# plt.show()
plt.savefig('/home/arthur/Dropbox/apresentacao_tese/images/detail_satk_time_op.png', dpi=500)

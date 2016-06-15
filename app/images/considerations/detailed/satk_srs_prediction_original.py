# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k
legend = ['SRS* Train', 'SRS* Pred',]

# S@K
srs_ = [5.486, 8.09, 9.722, 10.899, 11.797]
srs2_ = [13.088, 19.301, 23.195, 26.004, 28.146]

plt.plot(x, srs_, 'o--')
plt.plot(x, srs2_, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize=13)

# plt.show()
plt.savefig('/home/arthur/Dropbox/apresentacao_tese/images/detail_satk_srs_star_op.png', dpi=500)

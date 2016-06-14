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

plt.subplot(221)
plt.plot(x, srs_, 'o--')
plt.plot(x, srs2_, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# MRR
srs_ = [0.02993, 0.03339, 0.03468, 0.03534, 0.03573]
srs2_ = [0.0714, 0.07967, 0.08273, 0.08431, 0.08525]

plt.subplot(222)
plt.plot(x, srs_, 'o--')
plt.plot(x, srs2_, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('MRR', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Recall
srs_ = [0.00789, 0.01242, 0.01572, 0.01833, 0.02039]
srs2_ = [0.01882, 0.02964, 0.03751, 0.04373, 0.04866]

plt.subplot(223)
plt.plot(x, srs_, 'o--')
plt.plot(x, srs2_, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Recall', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Precision
srs_ = [0.00158, 0.00124, 0.00105, 0.00092, 0.00082]
srs2_ = [0.00376, 0.00296, 0.0025, 0.00219, 0.00195]

plt.subplot(224)
plt.plot(x, srs_, 'o--')
plt.plot(x, srs2_, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Precision', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

plt.show()
#plt.savefig('/home/arthur/work/tese/images/all_original.png', dpi=1850)

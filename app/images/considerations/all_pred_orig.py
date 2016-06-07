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

plt.subplot(221)
plt.plot(x, time, 'o--')
plt.plot(x, time2, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# MRR
time = [0.05071, 0.05697, 0.0595, 0.06085, 0.06169]
time2 = [0.06739, 0.07498, 0.0778, 0.07926, 0.08012]

plt.subplot(222)
plt.plot(x, time, 'o--')
plt.plot(x, time2, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('MRR', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Recall
time = [0.01146, 0.01754, 0.02196, 0.02551, 0.02852]
time2 = [0.01747, 0.02696, 0.03386, 0.03926, 0.04359]

plt.subplot(223)
plt.plot(x, time, 'o--')
plt.plot(x, time2, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Recall', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Precision
time = [0.00229, 0.00175, 0.00146, 0.00128, 0.00114]
time2 = [0.00349, 0.0027, 0.00226, 0.00196, 0.00174]

plt.subplot(224)
plt.plot(x, time, 'o--')
plt.plot(x, time2, '.-')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Precision', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

plt.show()
#plt.savefig('/home/arthur/work/tese/images/all_original.png', dpi=1850)

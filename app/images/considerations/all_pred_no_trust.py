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

plt.subplot(221)
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

# MRR
ucf = [0.01985, 0.0223, 0.02326, 0.02383, 0.02423]
srs = [0.04481, 0.04979, 0.05163, 0.05254, 0.05303]
srs_ = [0.0714, 0.07967, 0.08273, 0.08431, 0.08525]
tsrs = [0.02534, 0.02882, 0.03012, 0.03076, 0.03117]
tsrs_ = [0.0736, 0.08203, 0.08518, 0.08684, 0.08778]
time = [0.06739, 0.07498, 0.0778, 0.07926, 0.08012]

plt.subplot(222)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('MRR', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Recall
ucf = [0.00562, 0.00896, 0.01142, 0.01336, 0.01511]
srs = [0.01143, 0.01783, 0.0227, 0.02664, 0.02958]
srs_ = [0.01882, 0.02964, 0.03751, 0.04373, 0.04866]
tsrs = [0.00635, 0.01041, 0.01306, 0.01511, 0.01681]
tsrs_ = [0.0193, 0.03039, 0.03834, 0.04485, 0.04973]
time = [0.01747, 0.02696, 0.03386, 0.03926, 0.04359]

plt.subplot(223)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Recall', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Precision
ucf = [0.00112, 0.0009, 0.00076, 0.00067, 0.0006]
srs = [0.00229, 0.00178, 0.00151, 0.00133, 0.00118]
srs_ = [0.00376, 0.00296, 0.0025, 0.00219, 0.00195]
tsrs = [0.00127, 0.00104, 0.00087, 0.00076, 0.00067]
tsrs_ = [0.00386, 0.00304, 0.00256, 0.00224, 0.00199]
time = [0.00349, 0.0027, 0.00226, 0.00196, 0.00174]

plt.subplot(224)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Precision', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

plt.show()
#plt.savefig('/home/arthur/work/tese/images/all_original.png', dpi=1850)

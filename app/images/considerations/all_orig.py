# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS', 'TRS', 'HSRS']

# S@K
ucf = [2.383, 3.599, 4.399, 5.062, 5.669]
srs = [3.608, 5.266, 6.299, 7.017, 7.51]
srs_ = [5.486, 8.09, 9.722, 10.899, 11.797]
tsrs = [4.512, 7.024, 8.592, 9.682, 10.572]
tsrs_ = [5.706, 8.373, 10.053, 11.285, 12.188]
time = [9.372, 14.098, 17.325, 19.717, 21.633]
tnet = [30.039, 43.868, 50.602, 54.42, 56.892]
hsrs = [29.681, 43.725, 50.594, 54.587, 57.216]

plt.subplot(221)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.plot(x, hsrs, '>:')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# MRR
ucf = [0.013, 0.01461, 0.01524, 0.01561, 0.01588]
srs = [0.01989, 0.0221, 0.02292, 0.02333, 0.02354]
srs_ = [0.02993, 0.03339, 0.03468, 0.03534, 0.03573]
tsrs = [0.02416, 0.02748, 0.02872, 0.02933, 0.02972]
tsrs_ = [0.03085, 0.03438, 0.0357, 0.0364, 0.03679]
time = [0.05071, 0.05697, 0.0595, 0.06085, 0.06169]
tnet = [0.15269, 0.17132, 0.17666, 0.17882, 0.17991]
hsrs = [0.15059, 0.16947, 0.17492, 0.17717, 0.17833]

plt.subplot(222)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.plot(x, hsrs, '>:')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('MRR', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Recall
ucf = [0.00368, 0.00587, 0.00748, 0.00875, 0.0099]
srs = [0.00508, 0.00792, 0.01008, 0.01183, 0.01313]
srs_ = [0.00789, 0.01242, 0.01572, 0.01833, 0.02039]
tsrs = [0.00606, 0.00992, 0.01245, 0.01441, 0.01603]
tsrs_ = [0.00809, 0.01274, 0.01607, 0.0188, 0.02084]
time = [0.01146, 0.01754, 0.02196, 0.02551, 0.02852]
tnet = [0.05634, 0.08925, 0.10642, 0.11677, 0.12409]
hsrs = [0.0556, 0.08894, 0.10618, 0.11691, 0.12477]

plt.subplot(223)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.plot(x, hsrs, '>:')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Recall', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# Precision
ucf = [0.00074, 0.00059, 0.0005, 0.00044, 0.0004]
srs = [0.00102, 0.00079, 0.00067, 0.00059, 0.00053]
srs_ = [0.00158, 0.00124, 0.00105, 0.00092, 0.00082]
tsrs = [0.00121, 0.00099, 0.00083, 0.00072, 0.00064]
tsrs_ = [0.00162, 0.00127, 0.00107, 0.00094, 0.00083]
time = [0.00229, 0.00175, 0.00146, 0.00128, 0.00114]
tnet = [0.01127, 0.00892, 0.00709, 0.00584, 0.00496]
hsrs = [0.01112, 0.00889, 0.00708, 0.00585, 0.00499]

plt.subplot(224)
plt.plot(x, ucf, '.-')
plt.plot(x, srs, 'o--')
plt.plot(x, srs_, 'v-.')
plt.plot(x, tsrs, '>:')
plt.plot(x, tsrs_, '.-')
plt.plot(x, time, 'o--')
plt.plot(x, tnet, 'v-.')
plt.plot(x, hsrs, '>:')
plt.xlim((4, 26))
plt.xlabel('K', fontsize=18)
plt.ylabel('Precision', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

plt.show()
#plt.savefig('/home/arthur/work/tese/images/all_original.png', dpi=1850)

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k

## figure from original
ucf = [0.013, 0.01461, 0.01524, 0.01561, 0.01588]
srs = [0.01989, 0.0221, 0.02292, 0.02333, 0.02354]
srs_ = [0.02993, 0.03339, 0.03468, 0.03534, 0.03573]
tsrs = [0.02416, 0.02748, 0.02872, 0.02933, 0.02972]
tsrs_ = [0.03085, 0.03438, 0.0357, 0.0364, 0.03679]
time = [0.05071, 0.05697, 0.0595, 0.06085, 0.06169]
tnet = [0.15269, 0.17132, 0.17666, 0.17882, 0.17991]
hsrs = [0.15059, 0.16947, 0.17492, 0.17717, 0.17833]
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS', 'TRS', 'HSRS']

# plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
fig = plt.figure()

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

# plt.show()
fig.savefig('/home/arthur/work/tese/images/mrr_original.png', dpi=250)

## figure from prediction
ucf = [0.01985, 0.0223, 0.02326, 0.02383, 0.02423]
srs = [0.04481, 0.04979, 0.05163, 0.05254, 0.05303]
srs_ = [0.0714, 0.07967, 0.08273, 0.08431, 0.08525]
tsrs = [0.02534, 0.02882, 0.03012, 0.03076, 0.03117]
tsrs_ = [0.0736, 0.08203, 0.08518, 0.08684, 0.08778]
time = [0.06739, 0.07498, 0.0778, 0.07926, 0.08012]
tnet = [0.15972, 0.1792, 0.18479, 0.18704, 0.18818]
hsrs = [0.1506, 0.16948, 0.17493, 0.17718, 0.17834]
legend = ['UCF', 'SRS', 'SRS*', 'TSRS', 'TSRS*', 'Time-TSRS', 'TRS', 'HSRS']

# plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
fig = plt.figure()

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

# plt.show()
fig.savefig('/home/arthur/work/tese/images/mrr_prediction.png', dpi=250)

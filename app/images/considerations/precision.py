# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k

## figure from original
ucf = [0.00074, 0.00059, 0.0005, 0.00044, 0.0004]
srs = [0.00102, 0.00079, 0.00067, 0.00059, 0.00053]
srs_ = [0.00158, 0.00124, 0.00105, 0.00092, 0.00082]
tsrs = [0.00121, 0.00099, 0.00083, 0.00072, 0.00064]
tsrs_ = [0.00162, 0.00127, 0.00107, 0.00094, 0.00083]
time = [0.00229, 0.00175, 0.00146, 0.00128, 0.00114]
tnet = [0.01127, 0.00892, 0.00709, 0.00584, 0.00496]
hsrs = [0.01112, 0.00889, 0.00708, 0.00585, 0.00499]
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
plt.ylabel('Precision', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
fig.savefig('/home/arthur/work/tese/images/precision_original.png', dpi=250)

## figure from prediction
ucf = [0.00112, 0.0009, 0.00076, 0.00067, 0.0006]
srs = [0.00229, 0.00178, 0.00151, 0.00133, 0.00118]
srs_ = [0.00376, 0.00296, 0.0025, 0.00219, 0.00195]
tsrs = [0.00127, 0.00104, 0.00087, 0.00076, 0.00067]
tsrs_ = [0.00386, 0.00304, 0.00256, 0.00224, 0.00199]
time = [0.00349, 0.0027, 0.00226, 0.00196, 0.00174]
tnet = [0.01179, 0.00934, 0.00742, 0.00611, 0.00519]
hsrs = [0.01112, 0.00889, 0.00708, 0.00585, 0.00499]
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
plt.ylabel('Precision', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
fig.savefig('/home/arthur/work/tese/images/precision_prediction.png', dpi=250)

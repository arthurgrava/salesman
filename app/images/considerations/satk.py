# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k

## figure from original
ucf = [2.383, 3.599, 4.399, 5.062, 5.669]
srs = [3.608, 5.266, 6.299, 7.017, 7.51]
srs_ = [5.486, 8.09, 9.722, 10.899, 11.797]
tsrs = [4.512, 7.024, 8.592, 9.682, 10.572]
tsrs_ = [5.706, 8.373, 10.053, 11.285, 12.188]
time = [9.372, 14.098, 17.325, 19.717, 21.633]
tnet = [30.039, 43.868, 50.602, 54.42, 56.892]
hsrs = [29.681, 43.725, 50.594, 54.587, 57.216]
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
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
fig.savefig('/home/arthur/work/tese/images/satk_original.png', dpi=250)

## figure from prediction
ucf = [3.637, 5.494, 6.714, 7.725, 8.652]
srs = [8.127, 11.863, 14.187, 15.806, 16.917]
srs_ = [13.088, 19.301, 23.195, 26.004, 28.146]
tsrs = [4.732, 7.366, 9.011, 10.154, 11.087]
tsrs_ = [13.613, 19.977, 23.984, 26.924, 29.077]
time = [12.388, 18.112, 21.687, 24.282, 26.251]
tnet = [31.42, 45.885, 52.929, 56.922, 59.508]
hsrs = [29.683, 43.727, 50.597, 54.59, 57.22]
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
plt.ylabel('S@K', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
fig.savefig('/home/arthur/work/tese/images/satk_prediction.png', dpi=250)

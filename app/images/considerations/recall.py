# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# meaning to the plot
k = [5 * i for i in range(1, 6)]
x = k

## figure from original
ucf = [0.00368, 0.00587, 0.00748, 0.00875, 0.0099]
srs = [0.00508, 0.00792, 0.01008, 0.01183, 0.01313]
srs_ = [0.00789, 0.01242, 0.01572, 0.01833, 0.02039]
tsrs = [0.00606, 0.00992, 0.01245, 0.01441, 0.01603]
tsrs_ = [0.00809, 0.01274, 0.01607, 0.0188, 0.02084]
time = [0.01146, 0.01754, 0.02196, 0.02551, 0.02852]
tnet = [0.05634, 0.08925, 0.10642, 0.11677, 0.12409]
hsrs = [0.0556, 0.08894, 0.10618, 0.11691, 0.12477]
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
plt.ylabel('Recall', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
fig.savefig('/home/arthur/work/tese/images/recall_original.png', dpi=250)

## figure from prediction
ucf = [0.00562, 0.00896, 0.01142, 0.01336, 0.01511]
srs = [0.01143, 0.01783, 0.0227, 0.02664, 0.02958]
srs_ = [0.01882, 0.02964, 0.03751, 0.04373, 0.04866]
tsrs = [0.00635, 0.01041, 0.01306, 0.01511, 0.01681]
tsrs_ = [0.0193, 0.03039, 0.03834, 0.04485, 0.04973]
time = [0.01747, 0.02696, 0.03386, 0.03926, 0.04359]
tnet = [0.05893, 0.09335, 0.11132, 0.12214, 0.12979]
hsrs = [0.0556, 0.08895, 0.10618, 0.11692, 0.12478]
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
plt.ylabel('Recall', fontsize=16)
plt.legend(legend, loc='best', fontsize='x-small')

# plt.show()
fig.savefig('/home/arthur/work/tese/images/recall_prediction.png', dpi=250)

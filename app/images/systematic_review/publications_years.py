# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


index = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
values = [2, 1, 1, 3, 7, 10, 10, 10, 2]

WIDTH = 0.6
ALPHA = 0.4

plt.bar(np.arange(len(index)) + .5, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'ano')
plt.ylabel(u'quantidade de publicações')
plt.xticks(np.arange(len(index)) + (WIDTH / 2.0) + .5, index)
plt.tight_layout()
# plt.show()
plt.savefig('/home/arthur/work/tese/images/yearly_publication_distro.png', dpi=290)


### next one here... wherever
from matplotlib.ticker import FormatStrFormatter
years = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015",]

techniques = {
    "SRS": [1, 1, 2, 2, 4, 4, 1, 0, 0],
    "Mixed": [0, 0, 0, 0, 1, 1, 3, 10, 2],
    "CxF": [1, 0, 0, 0, 0, 0, 2, 0, 0],
    "LF": [0, 0, 0, 0, 1, 2, 0, 0, 0],
    "RWR": [0, 0, 1, 0, 0, 1, 0, 0, 0],
    "Others": [0, 0, 0, 0, 2, 2, 2, 0, 0],
}

colors = ['b', 'g', 'r', 'gray', 'c', 'm']
lines = ['-', '--', '-.', ':', '-', '-.', '--', ':']
markers = ['h', 'o', 'v', '^', 's', 'p']

fig = plt.figure()
ax = fig.add_subplot(111)

index = 0
for key, value in techniques.iteritems():
    ax.plot(years, value, label=key, color=colors[index], linestyle=lines[index], marker=markers[index])
    index += 1

ax.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

plt.ylim((-0.5, 10.5))
plt.xlim((2006.8, 2015.2))
plt.xlabel('ano')
plt.ylabel('quantidade')
plt.legend(loc=2)
plt.savefig('/home/arthur/work/tese/images/yearly_implemented_techiques.png', dpi=290)
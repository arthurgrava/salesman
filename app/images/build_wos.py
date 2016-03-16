# -*- coding: utf-8 -*-
import graphlab as gl
import graphlab.aggregate as agg
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

import matplotlib
matplotlib.get_backend()
​
ALPHA = 0.4
WIDTH = 0.6
DEVIATION = 0.1
MAX = 20
MAX_CIT = 100
​

# figure 1 - publications ditribution
data = gl.SFrame.read_csv('/home/arthur/work/images/wos/publications_per_author_distribution.csv')
hplus = data[data['publications'] > MAX]

labels = [str(data[i]['publications']) for i in range(0, MAX)]
values = [data[i]['contagem'] for i in range(0, MAX)]
labels.extend(['...', str(data[-1]['publications'])])
values.extend([hplus['contagem'].mean(), data[-1]['contagem']])

index = np.arange(len(labels))
plt.bar(index + DEVIATION, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'quantidade de publicações')
plt.ylabel(u'quantidade de autores')
plt.xticks(index + (WIDTH / 2.0) + DEVIATION, labels)
plt.legend()
plt.ylim((0.0, max(values) + 10000))
plt.tight_layout()
plt.show()
​

# figure 2 - citations distribuition
data = gl.SFrame.read_csv('/home/arthur/work/images/wos/citations_per_author_distribution.csv')

analyze = gl.SFrame()
analyze['citations'] = data.apply(lambda x: [x['citations'] for ele in range(0, x['contagem'])])
analyze = analyze.stack('citations', 'something')

hplus = data[data['citations'] > MAX_CIT]

labels = [str(data[i]['citations']) for i in range(0, MAX_CIT)]
values = [data[i]['contagem'] for i in range(0, MAX_CIT)]
labels.extend(['...', str(data[-1]['citations'])])
values.extend([hplus['contagem'].mean(), data[-1]['contagem']])

index = np.arange(len(labels))
plt.bar(index + DEVIATION, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'quantidade de publicações')
plt.ylabel(u'quantidade de autores')
plt.xticks(index + (WIDTH / 2.0) + DEVIATION, labels)
plt.legend()
plt.ylim((0.0, max(values) + 10000))
plt.tight_layout()
plt.show()
​
# figure 3 - years
data = gl.SFrame.read_csv('/home/arthur/work/images/wos/publications_per_year.csv')

labels = list(data['year'])
values = list(data['publications'])

index = np.arange(len(labels))
plt.bar(index + DEVIATION, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'ano de publicação')
plt.ylabel(u'quantidade de publicações')
plt.xticks(index + (WIDTH / 2.0) + DEVIATION, labels)
plt.legend()
plt.ylim((0.0, max(values) + 10000))
plt.tight_layout()
plt.show()
​
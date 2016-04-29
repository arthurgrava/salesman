# -*- coding: utf-8 -*-
import graphlab as gl
import matplotlib.pyplot as plt
import seaborn as sb


MAX = 20
data = gl.SFrame.read_csv('/home/arthur/work/images/wos/publications_per_author_distribution.csv')
hplus = data[data['publications'] > MAX]

index = [str(data[i]['publications']) for i in range(0, MAX)]
values = [data[i]['contagem'] for i in range(0, MAX)]
index.extend(['...', str(data[-1]['publications'])])
values.extend([hplus['contagem'].mean(), data[-1]['contagem']])

WIDTH = 0.6
ALPHA = 0.4

plt.bar(index, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'ano de publicação')
plt.ylabel(u'quantidade de publicações')
plt.ylim((min(values), max(values)))
plt.tight_layout()
plt.show()
# plt.savefig('/home/arthur/work/tese/images/publications_distribuition.png', dpi=290)

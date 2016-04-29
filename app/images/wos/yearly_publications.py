# -*- coding: utf-8 -*-
import graphlab as gl
import matplotlib.pyplot as plt
import seaborn as sb


data = gl.SFrame.read_csv('/home/arthur/work/images/wos/publications_per_year.csv')
WIDTH = 0.6
ALPHA = 0.4
index = list(data['year'])
values = list(data['publications'])

plt.bar(index, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'ano de publicação')
plt.ylabel(u'quantidade de publicações')
plt.xlim((min(values), max(values)))
plt.xlim((min(index), max(index)))
plt.tight_layout()
# plt.show()
plt.savefig('/home/arthur/work/tese/images/publications_over_the_years.png', dpi=290)

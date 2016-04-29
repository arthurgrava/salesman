# -*- coding: utf-8 -*-
import graphlab as gl
import matplotlib.pyplot as plt
import seaborn as sb

data = gl.SFrame.read_csv('/home/arthur/work/images/wos/citations_per_author_distribution.csv')
data = data.sort('citations')


WIDTH = .6
ALPHA = .4
index = list(data['citations'])[0:200]
values = list(data['contagem'])[0:200]

plt.bar(index, values, WIDTH, alpha=ALPHA, color='b')
plt.xlabel(u'quantidade de publicações')
plt.ylabel(u'quantidade de autores')
plt.xlim((0, max(values) + 5))
plt.xlim((0, max(index) + 5))
plt.tight_layout()
#plt.show()
plt.savefig('/home/arthur/work/tese/images/citations_distribution.png', dpi=290)

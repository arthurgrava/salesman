# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

from matplotlib.ticker import FormatStrFormatter

temp = ["F-Measure", "MAE ", "F-Measure", "Hit rate", "MAE", "RMSE", "MAE", "ROC Curve", "Hit rate", "MAE", "RMSE", "Precision", "Recall", "AUC", "F-Measure", "MAE", "ARR", "SD", "Hit rate", "Average Age", "MAP", "MPR", "MAE", "RMSE", "NDCG", "MRR-IA", "RMSE", "F-Measure", "MAE", "F-Measure", "Hit rate", "Hit rate", "Precision", "Recall", "APR", "RMSE", "Recall", "MAE", "Precision", "Recall", "AUC", "MAP", "AUC", "Precision", "Average Precision", "Acceptance", "MAE", "RMSE", "MAE", "TF-IDF Score", "RMSE", "MAE", "Acceptance", "Precision", "Recall", "Utiliy", "Coverage", "MAE", "RMSE", "MAE", "Precision", "Recall", "MAE", "RMSE", "Precision", "Coverage", "Hit rate", "Precision", "Recall", "F-Measure", "Global satisfaction", "RMSE", "MAE", "MAE", "MAE", "RMSE", "Recall", "MAE", "RMSE", "AUC", "MAE", "MAP", "F-Measure", "NDCG", "MAE", "RMSE"]
metrics = [item.strip() for item in temp]
single = set(metrics)

counting = {}
for metric in single:
    count = metrics.count(metric)
    if count > 2:
        counting[metric] = count

counting['Precision-Recall'] = counting['Precision']
del counting['Precision']
del counting['Recall']

metrics = ['MAP', 'AUC', 'Hit rate', 'F-Measure', 'Precision-Recall', 'RMSE', 'MAE']
appeared = [3, 4, 6, 7, 8, 13, 21]

alpha = 0.4
bar_width = 0.5
dev = 0.25
index = np.arange(len(appeared))

plt.bar(index + dev, appeared, bar_width, alpha=alpha, color='b')

plt.xlabel(u'métricas utilizadas')
plt.ylabel(u'quantidade')
plt.xticks(index + (bar_width / 2.0) + dev, metrics)
plt.legend()

plt.tight_layout()
plt.show()

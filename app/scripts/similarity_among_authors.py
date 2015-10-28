import graphlab as gl
import numpy


def pearson(a, b):
    """
    Pearson correlation between two maps
    """
    from scipy.stats.stats import pearsonr
    keys_a = a.keys()
    keys_b = b.keys()
    a_vector = []
    b_vector = []
    for key in keys_a:
        if key in keys_b:
            a_vector.append(float(a[key]))
            b_vector.append(float(b[key]))
    if not a_vector:
        return 0.0
    return pearsonr(a_vector, b_vector)[1]


ratings = gl.SFrame.read_csv('/Users/tutu/personal/git/data/authors_reference_single_line_without_counting.csv')

pearson(ratings[0]['ratings'], ratings[1]['ratings'])

author = []; compared_to = []; correlation = []
corr = gl.SFrame()
size = len(ratings)

for i in range(0, size):
    for j in range(0, size):
        if i != j:
            sim = pearson(ratings[i]['ratings'], ratings[j]['ratings'])
            author.append(ratings[i]['author'])
            compared_to.append(ratings[j]['author'])
            correlation.append(sim)
    similarity = gl.SFrame({'author': author, 'compared_to': compared_to, 'correlation': correlation})
    corr = corr.append(similarity.topk('correlation', k = 10))
    author = []; compared_to = []; correlation = []

corr.save('/Users/tutu/personal/git/data/author_pearson_correlated_without_counting.csv')

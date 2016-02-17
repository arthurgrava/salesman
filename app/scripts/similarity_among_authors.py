import graphlab as gl
import numpy
from scipy.stats.stats import pearsonr


def pearson(a, b):
    """
    Pearson correlation between two maps
    """
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

def calculate(begin, end):
    ratings = gl.SFrame.read_csv('/Users/tutu/personal/git/data/authors_reference_single_line_without_counting.csv')

    author = []; compared_to = []; correlation = []
    corr = gl.SFrame()
    size = len(ratings)

    for i in range(begin, end):
        for j in range(0, size):
            if i != j:
                sim = pearson(ratings[i]['ratings'], ratings[j]['ratings'])
                author.append(ratings[i]['author'])
                compared_to.append(ratings[j]['author'])
                correlation.append(sim)
        similarity = gl.SFrame({'author': author, 'compared_to': compared_to, 'correlation': correlation})
        corr = corr.append(similarity.topk('correlation', k = 20))
        similarity = None
        author = []; compared_to = []; correlation = []

    corr.save('/Users/tutu/personal/git/data/author_pearson_correlated_without_counting_{0}_{1}.csv'.format(begin, end))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Missing parameters indicating beginning and ending")

    begin = int(sys.argv[1])
    end = int(sys.argv[2])

    print u'Starting execution running it from {0} to {1}'.format(begin, end)

    calculate(begin, end)

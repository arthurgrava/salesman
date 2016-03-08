#encoding:utf-8
import graphlab as gl
import graphlab.aggregate as agg

"""
This script was created to generated the following files:
"""
# needed constants
AMOUNT_OF_PUBLISHED_ARTICLES = 24.0
BASE_PATH = '/home/arthur/work/data'
NORMALIZED_PATH = 'normalized' # when we count how many times the author has cited an article
UNORMALIZED_PATH = 'unormalized' # when we doesn't cara about how many times the author has cited an article

AUTHORS_PATH =  'authors_citations_full_{}.csv'.format(int(AMOUNT_OF_PUBLISHED_ARTICLES))
AUTHORS_MEANS_PATH = 'authors_means_{}.csv'.format(int(AMOUNT_OF_PUBLISHED_ARTICLES))

# loads the file and applies some filters
authors_data = gl.SFrame.read_csv('/home/arthur/work/data/authors_articles_referenced.csv', delimiter='\t', column_type_hints=[str, str, float])
authors_data = authors_data[authors_data['reference'] != '']


""" UNORMALIZED WAY OF SEING THE AUTHORS """
# this step removes lines that occurs more than one time (if the author has cited an article more than once)
deduplicated_authors_data = authors_data.unique()
aggregated_data = deduplicated_authors_data.groupby(
    key_columns='author',
    operations={'count': agg.COUNT()},
)

# filters publishers with lower citation rates
aggregated_data = aggregated_data[aggregated_data['count'] > AMOUNT_OF_PUBLISHED_ARTICLES]
print 'The amount of publishers is {}'.format(len(aggregated_data))

# just some checking
# authors = list(aggregated_data['author'])
# uauthors = aggregated_data['author'].unique()
# print len(authors) == len(uauthors)

# filter needed publishers on the real dataset
data = deduplicated_authors_data.filter_by(
    list(aggregated_data['author']),
    'author'
)
grouped_citations = data.groupby(
    key_columns='author',
    operations={'ratings': agg.CONCAT('reference', 'score')},
)

path = '{0}/{1}/{2}.csv'.format(BASE_PATH, UNORMALIZED_PATH, AUTHORS_PATH)
grouped_citations.save(path, format='csv')

# gets users mean ratings
means = data.groupby(
    key_columns='author',
    operations={'mean_score': agg.AVG('score')}
)
path = '{0}/{1}/{2}.csv'.format(BASE_PATH, UNORMALIZED_PATH, AUTHORS_MEANS_PATH)
means.save(path, format='csv')


""" NORMALIZED WAY OF SEING THE AUTHORS """
scored_data = authors_data.groupby(
    key_columns=['author', 'reference'],
    operations={'count': agg.COUNT()}
)
scored_data['score'] = scored_data['count'].apply(lambda x: float(x))
del scored_data['count']

aggregated_data = scored_data.groupby(
    key_columns='author',
    operations={'count': agg.COUNT()}
)
aggregated_data = aggregated_data[aggregated_data['count'] > AMOUNT_OF_PUBLISHED_ARTICLES]
print 'The amount of publishers is {}'.format(len(aggregated_data))

data = scored_data.filter_by(
    list(aggregated_data['author']),
    'author'
)

# normalizing score, what I'm doing is creating too many zeros
_max = float(data['score'].max())
_min = float(data['score'].min())
data['score'] = data['score'].apply(lambda x: ((float(x) - _min) / (_max - _min)) + 1)

# aggregates and saves the files
grouped_citations = data.groupby(
    key_columns='author',
    operations={'ratings': agg.CONCAT('reference', 'score')},
)
path = '{0}/{1}/{2}.csv'.format(BASE_PATH, NORMALIZED_PATH, AUTHORS_PATH)
grouped_citations.save(path, format='csv')

# gets users mean ratings
means = data.groupby(
    key_columns='author',
    operations={'mean_score': agg.AVG('score')}
)
path = '{0}/{1}/{2}.csv'.format(BASE_PATH, NORMALIZED_PATH, AUTHORS_MEANS_PATH)
means.save(path, format='csv')

print 'Script ended'
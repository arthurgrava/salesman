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

ORIGINAL =  'authors_citations_{}.csv'.format(int(AMOUNT_OF_PUBLISHED_ARTICLES))
AUTHORS_PATH =  'authors_citations_full_{}.csv'.format(int(AMOUNT_OF_PUBLISHED_ARTICLES))

PATH = BASE_PATH + '/authors_articles_referenced.csv'
authors_data = gl.SFrame.read_csv(PATH, delimiter='\t', column_type_hints=[str, str, float])

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
data['score'] = data['score'].apply(
    lambda x: round(
        ((float(x) - _min) / (_max - _min)) + 1, 3
    )
)
data['author'] = data['author'].apply(lambda x: hash(x))
data['reference'] = data['reference'].apply(lambda x: hash(x))

path = '{0}/{1}/{2}'.format(BASE_PATH, NORMALIZED_PATH, AUTHORS_PATH)
data.save(path, format='csv')
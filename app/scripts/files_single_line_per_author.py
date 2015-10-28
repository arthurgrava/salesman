#encoding:utf-8
import graphlab as gl
import graphlab.aggregate as agg


"""
Transformando o arquivo em 1 autor por linha com suas referências de duas maneiras
1- Marcando somente aqueles que foram citados
2- Fazendo contagens de quantas vezes um autor citou uma referência como score
"""
authors_data = gl.SFrame.read_csv('/Users/tutu/personal/git/data/authors_articles_referenced.csv', delimiter='\t', column_type_hints=[str, str, float])
authors_data = authors_data[authors_data['reference'] != '']

""" Attempt number one """
# this step removes lines that occurs more than one time (if the author has cited an article more than once)
sframe = authors_data.unique()
count = sframe.groupby(
    key_columns='author',
    operations={'count': agg.COUNT()}
)

# gets just the articles with more than 4 citations
print len(count)
count = count[count['count'] > 4.0]
print len(count)

# filter to use only the users mentioned above and groups all of theirs citations saving the result in a csv file
sframe = sframe.filter_by(count['author'].unique(), 'author')
grouped = sframe.groupby(
    key_columns='author',
    operations={'ratings': agg.CONCAT('reference', 'score')}
)
grouped.save('/Users/tutu/personal/git/data/authors_reference_single_line_without_counting.csv', format='csv')

# gl.distances.cosine(grouped[grouped['author'] == 'cornejo dr'][0]['ratings'], grouped[grouped['author'] == 'azevedo a'][0]['ratings'])

""" Attempt number two """
sframe = authors_data.groupby(
    key_columns=['author', 'reference'],
    operations={'count': agg.COUNT()}
)
sframe['score'] = sframe['count'].apply(lambda x: float(x))
del sframe['count']

count = sframe.groupby(
    key_columns='author',
    operations={'count': agg.COUNT()}
)

# gets just the articles with more than 4 citations
print len(count)
count = count[count['count'] > 4.0]
print len(count)

sframe = sframe.filter_by(count['author'].unique(), 'author')

# normalizing score
_max = float(sframe['score'].max())
_min = float(sframe['score'].min())
sframe['score'] = sframe['score'].apply(lambda x: (float(x) - _min) / (_max - _min))

grouped = sframe.groupby(
    key_columns='author',
    operations={'ratings': agg.CONCAT('reference', 'score')}
)
grouped.save('/Users/tutu/personal/git/data/authors_reference_single_line_with_counting.csv', format='csv')
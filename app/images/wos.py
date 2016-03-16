# -*- coding: utf-8 -*-
import re
import graphlab as gl
import graphlab.aggregate as agg


DOI_REGEX = re.compile(ur'\b(10[.][0-9]{4,}(?:[.][0-9]+)*\/(?:(?!["&\'<>])\S)+)\b')


data = gl.SFrame.read_csv('/home/arthur/work/data/wos_selected_filters.csv', column_type_hints=[str, str, str, str, int, str, str, str, str, str, str])
print(len(data))

data['array_authors'] = data['authors'].apply(lambda x: [item.strip().lower() for item in x.split(';')])
authors_list = []
for row in data:
    authors_list.extend(row['array_authors'])

authors = set(authors_list)
print(len(authors))

def _get_doi(citation):
    res = re.findall(DOI_REGEX, citation)
    return res[0] if res else None

# tst['citations_array'] = tst['citations'].apply(lambda x: [_get_doi(citation.strip().lower()) for citation in x.split(';')])
data['citations_array'] = data['citations'].apply(lambda x: [_get_doi(citation.strip().lower()) for citation in x.split(';')])
cit_list = []
for row in data:
    cit_list.extend(row['citations_array'])

citations = set(cit_list)
print(len(citations))

# pb = tst.stack('array_authors', 'author')
pubs = data.stack('array_authors', 'author')
citators = pubs.groupby('author', {'count': agg.COUNT}).sort('count', ascending=False)
citators['count'].sketch_summary()


# gb = pb.stack('citations_array', 'citation')
gb = pubs.stack('citations_array', 'citation')
citations = gb.groupby('author', {'count': agg.COUNT}).sort('count', ascending=False)
citations['count'].sketch_summary()

# aa
hist1 = citators.groupby('count', {'contagem': agg.COUNT}).sort('count', ascending=True)
hist2 = citations.groupby('count', {'contagem': agg.COUNT}).sort('count', ascending=True)

hist1.rename({'count': 'publications'})
hist2.rename({'count': 'citations'})

hist1.save('/home/arthur/work/images/wos/publications_per_author_distribution.csv', format='csv')
hist2.save('/home/arthur/work/images/wos/citations_per_author_distribution.csv', format='csv')

# year stuff
year = data[data['year'] > 1000]
print(year['year'].min())
print(year['year'].max())
yearly = year.groupby('year', {'publications': agg.COUNT}).sort('year')
yearly.save('/home/arthur/work/images/wos/publications_per_year.csv', format='csv')

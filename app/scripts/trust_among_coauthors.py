#encoding:utf-8
import sys


def run(source, target):
    import graphlab as gl
    import graphlab.aggregate as agg

    sf = gl.SFrame.read_csv(source, header=False)
    sf.rename({'X1': 'authorId', 'X2': 'similarId', 'X3': 'count'})

    _max = sf.groupby('authorId', {'_max': agg.MAX('count')})
    dict_max = {obj['authorId']: obj['_max'] for obj in _max.apply(lambda x: x, dtype=dict)}
    
    sf['trust'] = sf.apply(lambda x: x['count'] / dict_max[x['authorId']])
    sf.save(target, format='csv')

    del sf['count']
    sf.save(target + '.2', format='csv')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Run: python trust_among_coauthors.py {source} {target}')
    source = sys.argv[1]
    target = sys.argv[2]

    run(source, target)

#encoding:utf-8
import sys


def run(similarity, trust, target):
    import graphlab as gl
    
    sim = gl.SFrame.read_csv(similarity, header=False, column_type_hints=[str,str,float])
    sim.rename({'X1': 'authorId', 'X2': 'similarId', 'X3': 'score'})

    tst = gl.SFrame.read_csv(trust, column_type_hints=[str,str,float,float])

    sf = sim.join(tst, on=['authorId', 'similarId'])
    sf['trusted_score'] = sf.apply(lambda x: x['score'] * x['trust'])
    del sf['score']
    del sf['count']
    del sf['trust']
    sf.rename({'trusted_score': 'score'})

    similars = sf.sort(['authorId', 'score'], ascending=[True, False])
    similars.save(target, format='csv')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise Exception('Run:\n\tpython trust_similars.py {similars} {trust} {target}')

    similarity = '/home/arthur/work/data/files/similarity.csv'
    trust = '/home/arthur/work/data/files/trust_coauthors.csv'
    target = '/home/arthur/work/data/files/similarity_coauthors_trust.csv'

    run(similarity, trust, target)

#encoding:utf-8
import sys


COLUMNS = [
    'authorId', 
    'satk-5', 'satk-10', 'satk-15', 'satk-20', 'satk-25',
    'recall-5', 'recall-10', 'recall-15', 'recall-20', 'recall-25',
    'precision-5', 'precision-10', 'precision-15', 'precision-20', 'precision-25',
    'mrr-5', 'mrr-10', 'mrr-15', 'mrr-20', 'mrr-25',
]
K = 5

def _print(satk, mrr, recall, precision):
    print('\n' + ('-' * 79))
    print('| Score | k=5 | k=10 | k=15 | k=20 | k=25')
    print('| S@K | {}'.format(' | '.join([str(round(val, 5) * 100) for val in satk])))
    print('| MRR | {}'.format(' | '.join([str(round(val, 5)) for val in mrr])))
    print('| Recall | {}'.format(' | '.join([str(round(val, 5)) for val in recall])))
    print('| Precision | {}'.format(' | '.join([str(round(val, 5)) for val in precision])))
    print(('-' * 79) + '\n')


def calculate(filepath, n_ratings):
    import graphlab as gl
    sf = gl.SFrame.read_csv(filepath, header=False)

    cols = {'X{}'.format((idx + 1)): COLUMNS[idx] for idx in range(0, len(COLUMNS))}
    sf.rename(cols)

    satk = []
    mrr = []
    recall = []
    precision =[]

    for idx in range(1, 6):
        pos = idx * K
        satk.append(sf['satk-{}'.format(pos)].mean())
        mrr.append(sf['mrr-{}'.format(pos)].mean())
        recall.append(sf['recall-{}'.format(pos)].sum() / n_ratings)
        precision.append(sf['precision-{}'.format(pos)].sum() / n_ratings)


    _print(satk, mrr, recall, precision)


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        raise Exception("you must provide an evaluation file path and the number of ratings, e.g.:\n | python evaluation.py /tmp/eval.csv 234543")
    calculate(sys.argv[1], int(sys.argv[2]))

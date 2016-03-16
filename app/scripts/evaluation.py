#encoding:utf-8
import sys


COLUMNS = [
    'authorId', 
    'satk-5', 'satk-10', 'satk-15', 'satk-20', 'satk-25',
    'mae-5', 'mae-10', 'mae-15', 'mae-20', 'mae-25',
    'rmse-5', 'rmse-10', 'rmse-15', 'rmse-20', 'rmse-25',
    'mrr-5', 'mrr-10', 'mrr-15', 'mrr-20', 'mrr-25',
]
K = 5

def _print(satk, mrr, mae, rmse, maereg, rmsereg):
    print('\n' + ('-' * 79))
    print('| Score | k=5 | k=10 | k=15 | k=20 | k=25')
    print('| S@K | {}'.format(' | '.join([str(round(val, 5) * 100) for val in satk])))
    print('| MRR | {}'.format(' | '.join([str(round(val, 5)) for val in mrr])))
    print('| MAE | {}'.format(' | '.join([str(round(val, 5)) for val in mae])))
    print('| MAE* | {}'.format(' | '.join([str(round(val, 5)) for val in maereg])))
    print('| RMSE | {}'.format(' | '.join([str(round(val, 5)) for val in rmse])))
    print('| RMSE* | {}'.format(' | '.join([str(round(val, 5)) for val in rmsereg])))
    print(('-' * 79) + '\n')


def calculate(filepath):
    import graphlab as gl
    sf = gl.SFrame.read_csv(filepath, header=False)

    cols = {'X{}'.format((idx + 1)): COLUMNS[idx] for idx in range(0, len(COLUMNS))}
    sf.rename(cols)

    satk = []
    mrr = []
    mae = []
    maereg = []
    rmse =[]
    rmsereg = []

    for idx in range(1, 6):
        pos = idx * K
        satk.append(sf['satk-{}'.format(pos)].mean())
        mrr.append(sf['mrr-{}'.format(pos)].mean())
        mae.append(sf['mae-{}'.format(pos)].mean())
        rmse.append(sf['rmse-{}'.format(pos)].mean())
        maereg.append(sf[sf['mae-{}'.format(pos)] < 50.0]['mae-{}'.format(pos)].mean())
        rmsereg.append(sf[sf['rmse-{}'.format(pos)] < 50.0]['rmse-{}'.format(pos)].mean())


    _print(satk, mrr, mae, rmse, maereg, rmsereg)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception("you must provide a evaluation file path, e.g.:\n | python evaluation.py /tmp/eval.csv")
    calculate(sys.argv[1])

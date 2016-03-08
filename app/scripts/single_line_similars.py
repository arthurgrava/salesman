#encoding:utf-8
import sys


def run(source, target):
    import graphlab as gl
    import graphlab.aggregate as agg
    data = gl.SFrame.read_csv(source, delimiter=',', column_type_hints=[str, str, float], header=False)
    data.rename({'X1': 'author', 'X2': 'similar', 'X3': 'score'})
    grouped = data.groupby(
        key_columns='author',
        operations={'similars': agg.CONCAT('similar', 'score')}
    )
    grouped.save(target, format='csv')


if __name__ == '__main__':
    source = sys.argv[1]
    target = sys.argv[2]
    if not source or not target:
        raise Exception('You must specify a source and a target file path')
    run(source, target)

#encoding:utf-8
import graphlab as gl
import sys


def run_app(similarity_path, coauthors_path, target_path):
	similarity = gl.SFrame.read_csv(similarity_path, header=False)
	similarity.rename({'X1': 'authorId', 'X2': 'similarId', 'X3': 'similarity'})

	coauthors = gl.SFrame.read_csv(coauthors_path, header=False)
	coauthors.rename({'X1': 'authorId', 'X2': 'similarId', 'X3': 'count'})

	coauthors = coauthors.join(similarity, on=['authorId', 'similarId']).sort(['authorId', 'similarity'])
	del coauthors['count']

	coauthors.save(target_path, format='csv')


if __name__ == '__main__':
	if len(sys.argv) < 4:
		raise Exception('Missing parameters, run:\n\tpython x.py {similarity.path} {coauthors.path} {target.path}')

	run_app(sys.argv[1], sys.argv[2], sys.argv[3])

# -*- coding: utf-8 -*-
import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
IDXS = [5, 10, 15, 20, 25, 30]


def run(jar, mode):
    for idx in IDXS:
        path = '{}/{}/{}_neighbors'.format(PATH, mode, idx)
        for ff in os.listdir(path):
            command = 'java -Xmx25000m -jar {} --run {}'.format(
                jar,
                path + '/' + ff
            )
            os.system(command)
            #print(command)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Missing {jar file} as parameter')

    jar = str(sys.argv[1])

    run(jar, 'original')
    run(jar, 'prediction')

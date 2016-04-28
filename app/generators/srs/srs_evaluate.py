# -*- coding: utf-8 -*-
import os


NEIGHBORS = [5, 10, 15, 20, 25, 30]
BASE = os.path.dirname(os.path.abspath(__file__))


def get_file_string_original(n):
    string = 'app=evaluation_2\n'
    string = string + 'ratings.path=/home/arthur/data/config/evaluation/../../citations_test.csv\n'
    string = string + 'predictions.path=/home/arthur/data/results_2/{}_neighbors/srs_recommendations.csv\n'.format(n)
    string = string + 'target.path=/home/arthur/data/evaluation_2/original/{}_neighbors/srs.csv\n'.format(n)
    return string


def get_file_string_prediction(n):
    string = 'app=evaluation_3\n'
    string = string + 'ratings.path=/home/arthur/data/config/evaluation/../../citations_test.csv\n'
    string = string + 'predictions.path=/home/arthur/data/results_2/{}_neighbors/srs_recommendations.csv\n'.format(n)
    string = string + 'target.path=/home/arthur/data/evaluation_2/prediction/{}_neighbors/srs.csv\n'.format(n)
    return string


def write_original(n):
    content = get_file_string_original(n)
    path = '{}/original/{}_neighbors/srs.properties'.format(
        BASE,
        n
    )
    directory = '/'.join(path.split('/')[:-1])
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'w') as fout:
        fout.write(content)


def write_prediction(n):
    content = get_file_string_prediction(n)
    path = '{}/prediction/{}_neighbors/srs.properties'.format(
        BASE,
        n
    )
    directory = '/'.join(path.split('/')[:-1])
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'w') as fout:
        fout.write(content)


def run():
    for n in NEIGHBORS:
        write_original(n)
        write_prediction(n)
        

if __name__ == '__main__':
    run()

# -*- coding: utf-8 -*-
import os


NEIGHBORS = [5, 10, 15, 20, 25, 30]
BASE = os.path.dirname(os.path.abspath(__file__))


def get_file_string(neighbors):
    string = 'app=tsrs\n'
    string = string + 'top.k=50\n'
    string = string + 'citations.path=/home/arthur/data/normalized/citations_train_75.csv\n'
    string = string + 'similarity.path=/home/arthur/data/normalized/time_context_coauthors.csv\n'
    string = string + 'means.path=/home/arthur/data/normalized/authors_means_24.csv\n'
    string = string + 'target.path=/home/arthur/data/results_2/{}_neighbors/time_tsrs_recommendations.csv\n'.format(neighbors)
    string = string + 'authors.path=/home/arthur/data/normalized/authors_to_recommend.csv\n'
    string = string + 'core.size=3\n'
    string = string + 'max.size=30\n'
    string = string + 'top.neighbors={}\n'.format(neighbors)
    return string


def run():
    for n in NEIGHBORS:
        content = get_file_string(n)
        path = '{}/{}_neighbors/time_tsrs.properties'.format(
            BASE,
            n
        )
        directory = '/'.join(path.split('/')[:-1])
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'w') as fout:
            fout.write(content)


if __name__ == '__main__':
    run()

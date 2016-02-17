#encoding:utf-8
import graphlab as gl
import graphlab.aggregate as agg


"""
Generates the file to be used to cross coauthors
"""
FILEPATH = '/Users/tutu/personal/git/data/wos_selected.csv'


data = gl.SFrame.read_csv(FILEPATH, delimiter='\t')


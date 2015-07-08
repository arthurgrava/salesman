# encoding:utf-8
import pandas as pd
from salesman import cf


def _read_data(path):
    return pd.read_csv(path)


def run_cf_user_based_approach():
    method = cf.UserBased()
    model = method.calculate('here i must enter some data')
    
    return

if __name__ == '__main__':
    run_cf_user_based_approach()
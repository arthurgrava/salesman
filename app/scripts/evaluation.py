#encoding:utf-8
import graphlab as gl
import sys


def calculate(filepath):
    sf = gl.SFrame.read_csv(filepath, header=False)
    sf.rename({'X1': 'authorId', 'X2': 'satk', 'X3': 'mae', 'X4': 'rmse'})

    satk_all = sf['satk'].mean()
    satk_non_zero = sf[sf['satk'] != .0]['satk'].mean()
    mae = sf['mae'].mean()
    mae_reg = sf[sf['mae'] <= 2.0]['mae'].mean()
    rmse = sf['rmse'].mean()
    rmse_reg = sf[sf['rmse'] <= 2.0]['rmse'].mean()


    print((
        '\nS@K_ALL = {satkall}\n'
        'S@K_N0 = {satkn}\n'
        'MAE = {mae}\n'
        'MAE_REG = {maereg}\n'
        'RMSE = {rmse}\n'
        'RMSE_REG = {rmsereg}\n'
    ).format(satkall=satk_all, satkn=satk_non_zero, mae=mae, rmse=rmse, maereg=mae_reg, rmsereg=rmse_reg))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception("you must provide a evaluation file path, e.g.:\n\tpython evaluation.py /tmp/eval.csv")
    calculate(sys.argv[1])

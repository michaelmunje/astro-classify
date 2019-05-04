import numpy as np
import pandas as pd


def calc_conf_matrix(y_pred, y_actual):
    conf_matrix = np.zeros((4, 4))

    for pred_row, actual_row in zip(y_pred, y_actual):
        conf_matrix[pred_row, actual_row] += 1

    return conf_matrix


def eval_metrics(model_paths):

    valid_true = pd.read_csv(model_paths.valid_true)

    valid_pred = pd.read_csv(model_paths.valid_preds)

    valid_true = valid_true[valid_true.columns[0]].values

    valid_pred = valid_pred[valid_pred.columns[0]].values

    print(valid_true)

    print(valid_pred)

    conf_matrix = calc_conf_matrix(valid_pred, valid_true)

    print(calc_conf_matrix(valid_pred, valid_true))

    df = pd.DataFrame(conf_matrix, columns=['Spiral', 'Elliptical', 'Irregular', 'Other'])

    df.to_csv(model_paths.conf_matrix, index=False)
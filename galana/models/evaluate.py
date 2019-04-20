import numpy as np
import pandas as pd


def calc_conf_matrix(y_pred, y_actual):
    conf_matrix = np.zeros((y_pred.size(), y_pred.size()))

    for pred_row, actual_row in zip(y_pred, y_actual):
        conf_matrix[np.argmax(pred_row), np.argmax(actual_row)] += 1

    return conf_matrix


def eval_metrics(model_paths):

    valid_true = pd.read_csv(model_paths.valid_true).values()

    valid_pred = pd.read_csv(model_paths.valid_preds).values()

    return calc_conf_matrix(valid_pred, valid_true)

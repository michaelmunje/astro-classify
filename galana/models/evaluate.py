import numpy as np
import pandas as pd


def calc_conf_matrix(y_pred, y_actual):
    conf_matrix = np.zeros((3, 3), dtype=np.int8)

    for pred_row, actual_row in zip(y_pred, y_actual):
        conf_matrix[pred_row, actual_row] += 1

    return conf_matrix


def eval_metrics(model_paths):

    valid_true = pd.read_csv(model_paths.valid_true)
    valid_pred = pd.read_csv(model_paths.valid_preds)

    valid_true = valid_true[valid_true.columns[0]].values
    valid_pred = valid_pred[valid_pred.columns[0]].values

    conf_matrix = calc_conf_matrix(valid_pred, valid_true)

    classes = ['Elliptical', 'Irregular', 'Spiral']
    df = pd.DataFrame(conf_matrix, columns=[single_class + ' TRUE' for single_class in classes])
    df.insert(0, "", [single_class + ' PRED' for single_class in classes])
    df.to_csv(model_paths.conf_matrix, index=False)

    df_metrics = pd.DataFrame(columns=['CLASS', 'TRUE_POSITIVES', 'FALSE_POSITIVES', 'FALSE_NEGATIVES', 'TRUE NEGATIVES',
                                       'ACCURACY', 'ERROR RATE', 'RECALL', 'SPECIFICITY', 'PRECISION', 'HARMONIC_MEAN'])
    for i in range(len(classes)):
        true_positives = conf_matrix[i, i]
        false_positives = np.sum(conf_matrix[i, :]) - true_positives
        false_negatives = np.sum(conf_matrix[:, i]) - true_positives
        true_negatives = np.sum(conf_matrix) - true_positives - false_positives - false_negatives

        all_positives = true_positives + false_positives
        all_negatives = true_negatives + false_negatives

        accuracy = (true_positives + true_negatives) / (all_positives + all_negatives)
        error_rate = 1 - accuracy
        recall = true_positives / (true_positives + false_negatives)
        precision = true_positives / all_positives
        specificity = true_negatives / all_negatives
        harmonic_mean = (2 * precision * recall) / (precision + recall)

        df_metrics.loc[-1] = [classes[i], true_positives, false_positives, false_negatives, true_negatives,
                              accuracy, error_rate, recall, specificity, precision, harmonic_mean]
        df_metrics.index = df_metrics.index + 1
        df_metrics = df_metrics.sort_index()

    df_metrics.to_csv(model_paths.other_metrics, index=False)


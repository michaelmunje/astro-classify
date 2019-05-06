import numpy as np
import pandas as pd
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.models import load_model


def calc_conf_matrix(y_pred, y_actual):
    conf_matrix = np.zeros((3, 3), dtype=np.int32)

    for pred_row, actual_col in zip(y_pred, y_actual):
        conf_matrix[pred_row, actual_col] += 1

    return conf_matrix


def calculate_predictions(solutions, image_path, true, preds, model_to_predict_path):

    df = pd.read_csv(solutions)

    df_headers = list(df.columns)

    datagen = IDG(rescale=1. / 255.)

    generator = datagen.flow_from_dataframe(
        dataframe=df,
        directory=image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        class_mode='categorical',
        shuffle=False,
        batch_size=24,
        seed=42,
        target_size=(200, 200))

    STEP_SIZE = generator.n // generator.batch_size + 1

    model = load_model(model_to_predict_path)

    print("Calculating predictions...")

    y_all_preds = model.predict_generator(generator=generator, steps=STEP_SIZE, use_multiprocessing=True)

    y_preds = list(y_all_preds.argmax(axis=-1))

    y_actuals = generator.classes

    pd.DataFrame(y_preds).to_csv(preds, index=False)

    pd.DataFrame(y_actuals).to_csv(true, index=False)

    print("Saved predictions to: " + preds)

    print("Saved actuals to: " + true)


def eval_metrics(true, preds, conf_matrix_path, other_metrics_path):

    true = pd.read_csv(true)
    pred = pd.read_csv(preds)

    true = true[true.columns[0]].values
    pred = pred[pred.columns[0]].values

    conf_matrix = calc_conf_matrix(pred, true)

    classes = ['Elliptical', 'Irregular', 'Spiral']
    df = pd.DataFrame(conf_matrix, columns=[single_class + ' TRUE' for single_class in classes])
    df.insert(0, "", [single_class + ' PRED' for single_class in classes])
    df.to_csv(conf_matrix_path, index=False)

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
        if all_positives > 0:
            precision = true_positives / all_positives
        elif true_negatives == 0:
            precision = 0
        else:
            precision = np.Inf

        if all_negatives > 0:
            specificity = true_negatives / all_negatives
        elif true_negatives == 0:
            specificity = 0
        else:
            specificity = np.Inf

        if precision != np.Inf:
            harmonic_mean = (2 * precision * recall) / (precision + recall)
        else:
            harmonic_mean = 'DNE'

        df_metrics.loc[-1] = [classes[i], true_positives, false_positives, false_negatives, true_negatives,
                              accuracy, error_rate, recall, specificity, precision, harmonic_mean]
        df_metrics.index = df_metrics.index + 1
        df_metrics = df_metrics.sort_index()

    df_metrics.to_csv(other_metrics_path, index=False)

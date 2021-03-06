import os
import pathlib as pl


class ModelPaths:  # Quick hack to make struct-like objects in python
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


def initialize_default_paths():
    model_paths = ModelPaths()
    model_paths.test_image_path = os.getcwd() + '/data/test_images/'
    model_paths.train_image_path = os.getcwd() + '/data/images_training_rev1/'
    model_paths.valid_image_path = os.getcwd() + '/data/valid_images/'

    if os.path.isfile(model_paths.test_image_path):
        model_paths.test_image_files = os.listdir(model_paths.test_image_path)
    else:
        model_paths.test_image_files = []

    if os.path.isfile(model_paths.valid_image_path):
        model_paths.valid_image_files = os.listdir(model_paths.test_image_path)
    else:
        model_paths.valid_image_files = []

    if os.path.isfile(model_paths.train_image_path):
        model_paths.train_image_files = os.listdir(model_paths.train_image_path)
    else:
        model_paths.train_image_files = []

    model_paths.all_solutions = os.getcwd() + '/data/solutions/training_solutions_rev1.csv'
    model_paths.clean_solutions = os.getcwd() + '/data/solutions/clean_solutions.csv'

    model_paths.clean_train_solutions = os.getcwd() + '/data/solutions/train_clean_solutions.csv'
    model_paths.augmented_train_solutions = os.getcwd() + '/data/solutions/train_augmented_solutions.csv'

    model_paths.valid_solutions = os.getcwd() + '/data/solutions/valid_solutions.csv'
    model_paths.test_solutions = os.getcwd() + '/data/solutions/test_solutions.csv'

    model_paths.test_file = os.getcwd() + '/data/all_zeros_benchmark.csv'

    model_paths.output_model_file = os.getcwd() + '/data/models/galaxy_classifier_model.json'
    model_paths.output_model_weights = os.getcwd() + '/data/models/galaxy_classifier_weights.h5'

    model_paths.checkpoint_path = os.getcwd() + "/data/models/checkpoints/{epoch:02d}-{val_acc:.2f}.hdf5"
    model_paths.checkpoint_overall_path = os.getcwd() + "/data/models/best_overall_model.hdf5"

    model_paths.valid_true = os.getcwd() + "/data/eval/valid/true.csv"
    model_paths.valid_preds = os.getcwd() + "/data/eval/valid/preds.csv"

    model_paths.test_true = os.getcwd() + "/data/eval/test/true.csv"
    model_paths.test_preds = os.getcwd() + "/data/eval/test/preds.csv"

    model_paths.valid_conf_matrix = os.getcwd() + "/data/eval/valid_conf_matrix.csv"
    model_paths.valid_other_metrics = os.getcwd() + "/data/eval/valid_other_metrics.csv"

    model_paths.test_conf_matrix = os.getcwd() + "/data/eval/test_conf_matrix.csv"
    model_paths.test_other_metrics = os.getcwd() + "/data/eval/test_other_metrics.csv"

    pl.Path(model_paths.test_image_path).mkdir(parents=True, exist_ok=True)
    pl.Path(model_paths.train_image_path).mkdir(parents=True, exist_ok=True)
    pl.Path(model_paths.valid_image_path).mkdir(parents=True, exist_ok=True)
    pl.Path(os.getcwd() + '/data/models/').mkdir(parents=True, exist_ok=True)
    pl.Path(os.getcwd() + '/data/models/checkpoints/').mkdir(parents=True, exist_ok=True)
    pl.Path(os.getcwd() + '/data/solutions/').mkdir(parents=True, exist_ok=True)
    pl.Path(os.getcwd() + '/data/eval/valid/').mkdir(parents=True, exist_ok=True)
    pl.Path(os.getcwd() + '/data/eval/test/').mkdir(parents=True, exist_ok=True)

    return model_paths


def initialize_custom_paths(test_images_p, valid_images_p, train_images_p, train_sol, clean_sols, augmented_sols, valid_sols, test_sols,
                            test_f, output_model_f, output_model_w, checkpoint_p, checkpoint_p_overall, valid_conf_matrix, valid_other_metrics,
                            test_conf_matrix, test_other_metrics, val_true, val_preds, test_preds, test_true):
    model_paths = ModelPaths()
    model_paths.test_image_path = test_images_p
    model_paths.train_image_path = train_images_p
    model_paths.valid_image_path = valid_images_p

    if os.path.isfile(model_paths.test_image_path):
        model_paths.test_image_files = os.listdir(model_paths.test_image_path)
    else:
        model_paths.test_image_files = []

    if os.path.isfile(model_paths.train_image_path):
        model_paths.train_image_files = os.listdir(model_paths.train_image_path)
    else:
        model_paths.train_image_files = []

        if os.path.isfile(model_paths.valid_image_path):
            model_paths.valid_image_files = os.listdir(model_paths.test_image_path)
        else:
            model_paths.valid_image_files = []

    model_paths.all_solutions = train_sol
    model_paths.clean_train_solutions = clean_sols
    model_paths.augmented_train_solutions = augmented_sols
    model_paths.valid_solutions = valid_sols
    model_paths.test_solutions = test_sols

    model_paths.test_file = test_f
    model_paths.output_model_file = output_model_f
    model_paths.output_model_weights = output_model_w
    model_paths.checkpoint_path = checkpoint_p
    model_paths.checkpoint_overall_path = checkpoint_p_overall
    model_paths.valid_true = val_true
    model_paths.valid_preds = val_preds
    model_paths.test_true = test_true
    model_paths.test_preds = test_preds
    model_paths.valid_conf_matrix = valid_conf_matrix
    model_paths.valid_other_metrics = valid_other_metrics
    model_paths.test_conf_matrix = test_conf_matrix
    model_paths.test_other_metrics = test_other_metrics

    return model_paths

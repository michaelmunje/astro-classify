import pytest
from galana import models
import os


def test_default_paths():
    model_paths = models.initialize_default_paths()
    assert(model_paths.test_image_path == os.getcwd() + '/data/kaggle/images_test_rev1/')
    assert(model_paths.test_image_files == [])
    assert(model_paths.train_image_path == os.getcwd() + '/data/kaggle/images_training_rev1/')
    assert(model_paths.train_image_files == [])
    assert(model_paths.train_solutions == os.getcwd() + '/data/kaggle/training_solutions_rev1.csv')
    assert(model_paths.clean_train_solutions == os.getcwd() + '/data/kaggle/clean_training_solutions_rev1.csv')
    assert(model_paths.test_file == os.getcwd() + '/data/kaggle/all_zeros_benchmark.csv')
    assert(model_paths.output_model_file == os.getcwd() + '/data/kaggle/galaxy_classifier_model.json')
    assert(model_paths.output_model_weights == os.getcwd() + '/data/kaggle/galaxy_classifier_weights.h5')
    assert(model_paths.checkpoint_path == "data/kaggle/checkpoint-{epoch:02d}-{val_acc:.2f}.hdf5")
    assert(model_paths.valid_true == "data/kaggle/valid_true.csv")
    assert(model_paths.valid_preds == "data/kaggle/valid_preds.csv")


if __name__ == '__main__':
    pytest.main([__file__])

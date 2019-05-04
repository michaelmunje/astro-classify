import pytest
from galana import models
import os


def test_default_paths():
    model_paths = models.initialize_default_paths()
    assert(model_paths.test_image_path == os.getcwd() + '/data/kaggle/images_test_rev1/')
    assert(model_paths.train_image_path == os.getcwd() + '/data/kaggle/images_training_rev1/')
    assert(model_paths.test_image_files == [])
    assert(model_paths.train_image_files == [])

    assert(model_paths.train_solutions == os.getcwd() + '/data/kaggle/solutions/training_solutions_rev1.csv')
    assert(model_paths.clean_train_solutions == os.getcwd() + '/data/kaggle/solutions/clean_solutions.csv')
    assert(model_paths.augmented_solutions == os.getcwd() + '/data/kaggle/solutions/augmented_solutions.csv')

    assert(model_paths.test_file == os.getcwd() + '/data/kaggle/all_zeros_benchmark.csv')
    assert(model_paths.output_model_file == os.getcwd() + '/data/kaggle/models/galaxy_classifier_model.json')
    assert(model_paths.output_model_weights == os.getcwd() + '/data/kaggle/models/galaxy_classifier_weights.h5')

    assert(model_paths.checkpoint_outer_path == os.getcwd() + "/data/kaggle/models/best_outer_model.hdf5")
    assert(model_paths.checkpoint_overall_path == os.getcwd() + "/data/kaggle/models/best_overall_model.hdf5")

    assert(model_paths.conf_matrix == os.getcwd() + "/data/kaggle/eval/conf_matrix.csv")
    assert(model_paths.other_metrics == os.getcwd() + "/data/kaggle/eval/other_metrics.csv")

    assert(model_paths.valid_true == os.getcwd() + "/data/kaggle/eval/valid/true.csv")
    assert(model_paths.valid_preds == os.getcwd() + "/data/kaggle/eval/valid/preds.csv")

    assert(model_paths.test_true == os.getcwd() + "/data/kaggle/eval/test/true.csv")
    assert(model_paths.test_preds == os.getcwd() + "/data/kaggle/eval/test/preds.csv")


def test_custom_paths():
    model_paths = models.initialize_custom_paths(test_images_p="asdf", train_images_p="gggg", train_sol='1234', clean_sols='pl', augmented_sols='hello',
                                                 test_f='wswqsas/wdowdw.pt', output_model_f='ssqqas/wdowdw.pt', output_model_w='wwswqa/wdowdw.pt',
                                                 checkpoint_p_outer='aaaa/aaaa.a', conf_matrix='c.c', other_metrics='a', checkpoint_p_overall='aaaa/aaab.a',
                                                 val_true='bb', val_preds='c.c', test_true='bb', test_preds='c.c')
    assert(model_paths.test_image_path == "asdf")
    assert(model_paths.train_image_path == "gggg")
    assert(model_paths.test_image_files == [])
    assert(model_paths.train_image_files == [])
    assert(model_paths.train_solutions == '1234')
    assert(model_paths.clean_train_solutions == 'pl')
    assert(model_paths.augmented_solutions == 'hello')
    assert(model_paths.test_file == 'wswqsas/wdowdw.pt')
    assert(model_paths.output_model_file == 'ssqqas/wdowdw.pt')
    assert(model_paths.output_model_weights == 'wwswqa/wdowdw.pt')
    assert(model_paths.checkpoint_outer_path == 'aaaa/aaaa.a')
    assert(model_paths.checkpoint_overall_path == 'aaaa/aaab.a')
    assert(model_paths.valid_true == 'bb')
    assert(model_paths.valid_preds == 'c.c')
    assert(model_paths.test_true == 'bb')
    assert(model_paths.test_preds == 'c.c')
    assert(model_paths.conf_matrix == 'c.c')
    assert(model_paths.other_metrics == 'a')


if __name__ == '__main__':
    pytest.main([__file__])

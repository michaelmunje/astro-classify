from galana import preprocessing
import os
import filecmp
import pytest


def test_preprocessing():
    root_dir = os.getcwd()
    input_dir = os.path.join(os.sep, root_dir, 'tests', 'preprocessing', 'input', 'preprocess_data')
    output_dir = os.path.join(os.sep, root_dir, 'tests', 'preprocessing', 'output', 'preprocess_data')
    expected_dir = os.path.join(os.sep, root_dir, 'tests', 'preprocessing', 'output', 'preprocess_data')

    preprocessing.preprocess_folder(input_dir, output_dir)

    for filename in os.listdir(expected_dir):
        assert(filecmp.cmp(expected_dir + '/' + filename, output_dir + '/' + filename, shallow=False) is True)


if __name__ == '__main__':
    pytest.main([__file__])

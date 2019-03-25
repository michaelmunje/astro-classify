from galana import preprocessing
import os
import filecmp
import pytest


def test_merging():
    root_dir = os.getcwd()
    input_dir = os.path.join('tests', 'preprocessing', 'input', 'merge')
    output_dir = os.path.join('tests', 'preprocessing', 'output', 'merge')
    expected_dir = os.path.join('tests', 'preprocessing', 'output', 'merge')

    expected_filepath = os.path.join(os.sep, root_dir, expected_dir, 'output.txt')
    output_filepath = os.path.join(os.sep, root_dir, output_dir, 'output.txt')

    preprocessing.merge(input_dir, output_filepath)

    assert(filecmp.cmp(expected_filepath, output_filepath, shallow=False) is True)


if __name__ == '__main__':
    pytest.main([__file__])

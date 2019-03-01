import astroclassify as ac
import os
import filecmp
import pytest


def test_merging():
    root_dir = os.getcwd()
    input_dir = os.path.join('tests', 'pipeline', 'test_input', 'merge')
    output_dir = os.path.join('tests', 'pipeline', 'test_output', 'merge')

    foldername = os.path.join(os.sep, root_dir, input_dir, 'to_merge')
    expected_filepath = os.path.join(os.sep, root_dir, input_dir, 'expected', 'expected_output.txt')
    output_filepath = os.path.join(os.sep, root_dir, output_dir, 'output.txt')

    ac.pipeline.merge(foldername, output_filepath)

    assert(filecmp.cmp(expected_filepath, output_filepath, shallow=False) is True)


if __name__ == '__main__':
    pytest.main([__file__])

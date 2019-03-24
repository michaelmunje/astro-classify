import pytest
import galana as ga
import os


def test_script_outputs():
    root_dir = os.getcwd()
    input_dir = os.path.join(root_dir, 'tests', 'xamin', 'helpers', 'test_input', 'script_output')
    test_file = os.path.join(input_dir, 'test_bash.sh')
    input = 'echo hello friends'
    assert(ga.xamin.helpers.get_inline_script_output(input) == 'hello friends\n')
    assert(ga.xamin.helpers.get_script_output(test_file) == 'hello world\n')


if __name__ == '__main__':
    pytest.main([__file__])

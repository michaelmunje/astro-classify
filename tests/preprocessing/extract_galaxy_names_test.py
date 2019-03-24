import pytest
import galana as ga
import os


def test_galaxy_name_extraction():
    root_dir = os.getcwd()
    input_dir = os.path.join('tests', 'pipeline', 'test_input', 'galaxy_name_extraction')
    filename = os.path.join(os.sep, root_dir, input_dir, 'RAW_NASA_DATABASE_TABLE')
    df = ga.preprocessing.extract_galaxy_names(filename)
    print(df['names'])
    assert(len(df['names']) == 3)
    if len(df['names']) == 3:
        assert(df['names'][0] == "SOME GALAXY")
        assert(df['names'][1] == "ANOTHER GALAXY")
        assert(df['names'][2] == "LAST ONE")


if __name__ == '__main__':
    pytest.main([__file__])

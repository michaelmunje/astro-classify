import pytest
from galana import preprocessing
import os


def test_kaggle():
    root_dir = os.getcwd()
    input_dir = os.path.join('tests', 'preprocessing', 'input', 'galaxy_name_extraction')
    filename = os.path.join(os.sep, root_dir, input_dir, 'RAW_NASA_DATABASE_TABLE')
    galaxy_list = preprocessing.extract_galaxy_names(filename)
    assert(len(galaxy_list) == 3)
    if len(galaxy_list) == 3:
        assert(galaxy_list[0] == "SOME GALAXY")
        assert(galaxy_list[1] == "ANOTHER GALAXY")
        assert(galaxy_list[2] == "LAST ONE")


if __name__ == '__main__':
    pytest.main([__file__])

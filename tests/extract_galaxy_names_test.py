import pytest
import astroclassify as ac
import pandas as pd


def test_galaxy_name_extraction():
    filename = "tests/test_cases/RAW_NASA_DATABASE_TABLE"
    df = ac.data.extract_galaxy_names(filename)
    assert(len(list(df)) == 3)


if __name__ == '__main__':
    pytest.main([__file__])

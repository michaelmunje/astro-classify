import pytest
import astroclassify as ac


def test_galaxy_name_extraction():
    filename = "tests/test_cases/RAW_NASA_DATABASE_TABLE"
    df = ac.data.extract_galaxy_names(filename)
    print(df['names'])
    assert(len(df['names']) == 3)
    if (len(df['names']) == 3):
        assert(df['names'][0] == "SOME GALAXY")
        assert(df['names'][1] == "ANOTHER GALAXY")
        assert(df['names'][2] == "LAST ONE")


if __name__ == '__main__':
    pytest.main([__file__])

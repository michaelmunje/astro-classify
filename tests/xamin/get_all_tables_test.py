import pytest
import galana as ga


def test_get_all_tables():
    ga.xamin.install()
    result = ga.xamin.get_all_names()
    assert(len(result) == 102)
    assert(result[0] == "a2pic.txt")


if __name__ == '__main__':
    pytest.main([__file__])

import pytest
from galana import xamin


@pytest.mark.skip(reason="Xamin is down.")
def test_get_all_tables():
    xamin.install()
    result = xamin.get_all_names()
    assert(len(result) == 102)
    assert(result[0] == "a2pic.txt")


if __name__ == '__main__':
    pytest.main([__file__])

import pytest
import sys


def test_associativity():
    assert (5 + 2) == (2 + 5)


def test_multiply():
    assert (5 * 1) == 5


def test_py3():
    assert(sys.version_info[0] >= 3)


if __name__ == '__main__':
    pytest.main([__file__])

import pytest
import sys


def test_py3():
    assert(sys.version_info[0] >= 3)

if __name__ == '__main__':
    pytest.main([__file__])

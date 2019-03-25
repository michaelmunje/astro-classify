from galana import ned
import pytest


def test_query():
    assert(ned.query_object('m77').iloc[0, 1] == b'MESSIER 077')
    assert(ned.query_object('andromeda galaxy').iloc[0, 1] == b'MESSIER 031')
    df = ned.query_objects(['m31', 'cgmw 1-1'])
    print(df)
    assert(df.iloc[0, 0] == b'MESSIER 031')
    assert(df.iloc[1, 0] == b'IRAS  06088+0221')


if __name__ == '__main__':
    pytest.main([__file__])

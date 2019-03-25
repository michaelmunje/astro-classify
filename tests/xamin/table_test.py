import pytest
import os
import pathlib as pl
from galana import xamin

root_dir = os.getcwd()
raw_data_dir = root_dir + '/data/mine/raw'
abs_raw_data_path = os.path.abspath(raw_data_dir)
pl.Path(abs_raw_data_path).mkdir(parents=True, exist_ok=True)


@pytest.mark.skip(reason="Xamin is down.")
def test_get_table():
    xamin.install()
    xamin.run_table_query("a2pic")
    assert(os.path.isfile(abs_raw_data_path + "a2pic.txt"))
    f = open(abs_raw_data_path + "a2pic.txt", "r")
    assert(f.readline().startswith("__row|a1name"))
    assert(f.readline().endswith("-0.9800"))
    f.close()


if __name__ == '__main__':
    pytest.main([__file__])

import pytest
from galana import preprocessing
import pandas as pd
import os


def test_kaggle():
    root_dir = os.getcwd()
    input_dir = os.path.join('tests', 'preprocessing', 'input', 'kaggle')
    inname = os.path.join(os.sep, root_dir, input_dir, 'solutions.csv')
    output_dir = os.path.join('tests', 'preprocessing', 'output', 'kaggle')
    outname = os.path.join(os.sep, root_dir, output_dir, 'solutions.csv')

    preprocessing.process_kaggle(inname, outname)

    df = pd.read_csv(inname)
    dfProcessed = pd.read_csv(outname)

    proc_galaxy1 = dfProcessed.iloc[0]
    proc_galaxy2 = dfProcessed.iloc[1]
    proc_galaxy3 = dfProcessed.iloc[2]

    assert(proc_galaxy1['Type'] == 'Spiral')
    assert(proc_galaxy2['Type'] == 'Spiral')
    assert(proc_galaxy3['Type'] == 'Elliptical')


if __name__ == '__main__':
    pytest.main([__file__])

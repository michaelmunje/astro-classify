#!/bin/bash
conda create -y --name galana
source activate galana
conda install -y --quiet --yes \
    'numpy' \
    'pandas' \
    'tensorflow' \
    'pytest' \
    'pytest-cov' \
    'keras' \
    'pillow'
conda clean -tipsy
pip install pytest-cov
conda install -y -c astropy astroquery
pip uninstall -y keras-preprocessing
pip install git+https://github.com/keras-team/keras-preprocessing.git

#!/bin/bash
conda create -y --name galana
source activate galana
conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'pytest' \
    'keras' \
    'pytest-cov' \
    'matplotlib' \
    'pillow' \
    'jupyter' \
    'tensorflow-gpu'
pip install 'jupyter-tensorboard'
pip install 'boto3'
conda clean -tipsy
conda install -c --yes astropy astroquery
#apt-get install -y libsm6 libxext6 libxrender-dev && \
pip uninstall -y keras-preprocessing && \
pip install git+https://github.com/keras-team/keras-preprocessing.git

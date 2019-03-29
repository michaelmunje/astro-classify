ARG BASE_CONTAINER=tensorflow/tensorflow:devel-gpu
FROM $BASE_CONTAINER

LABEL maintainer="tensorflow"

RUN pip install \
    'numpy' \
    'pandas' \
    'pytest' \
    'pytest-cov' \
    'keras' && \
    conda install openjdk && \
    conda clean -tipsy && \
    pip install pytest-cov && \
    pip install astropy && \
    mkdir .astropy && \
    pip uninstall -y keras-preprocessing && \
    pip install git+https://github.com/keras-team/keras-preprocessing.git && \
    chmod 667 .astropy

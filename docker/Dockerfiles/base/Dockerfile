ARG BASE_CONTAINER=continuumio/miniconda3
FROM $BASE_CONTAINER

LABEL maintainer="continuumio"

RUN conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'tensorflow-gpu' \
    'pytest' \
    'pytest-cov' \
    'keras' && \
    conda install openjdk && \
    conda clean -tipsy && \
    pip install pytest-cov && \
    conda install -c astropy astroquery && \
    mkdir .astropy && \
    pip uninstall -y keras-preprocessing && \
    pip install git+https://github.com/keras-team/keras-preprocessing.git && \
    chmod 667 .astropy

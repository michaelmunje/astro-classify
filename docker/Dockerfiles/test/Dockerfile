ARG BASE_CONTAINER=continuumio/miniconda
FROM $BASE_CONTAINER

LABEL maintainer="continuumio"

RUN conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'tensorflow=1.12*' \
    'pytest' \
    'keras=2.2*' && \
    conda clean -tipsy


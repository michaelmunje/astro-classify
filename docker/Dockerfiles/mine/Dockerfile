ARG BASE_CONTAINER=continuumio/miniconda3
FROM $BASE_CONTAINER

LABEL maintainer="continuumio"

RUN conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'selenium' && \
    conda install openjdk && \
    conda clean -tipsy && \
    pip install astroquery

CMD bash -c 'cd galana;bash'

ARG BASE_CONTAINER=continuumio/miniconda
FROM $BASE_CONTAINER

LABEL maintainer="continuumio"

RUN conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'selenium' && \
    conda clean -tipsy

CMD bash -c 'cd astro-classify;bash'

ARG BASE_CONTAINER=luke035/nvidia-anaconda-docker
FROM $BASE_CONTAINER

LABEL maintainer=""

RUN conda update -n base conda && \
    conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'pytest' \
    'keras' \
    'pytest-cov' && \
    conda install openjdk && \
    conda clean -tipsy && \
    pip install pytest-cov && \
    conda install -c astropy astroquery && \
    mkdir .astropy && \
    pip uninstall -y keras-preprocessing && \
    pip install git+https://github.com/keras-team/keras-preprocessing.git && \
    chmod 667 .astropy

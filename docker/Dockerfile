ARG BASE_CONTAINER=luke035/nvidia-anaconda-docker
FROM $BASE_CONTAINER

LABEL maintainer=""

RUN apt-get update && \
    apt-get upgrade -y && \
    conda update -n base conda && \
    pip install --upgrade pip && \
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
    chmod 667 .astropy && \
    apt-get install -y git && \
    pip uninstall -y keras-preprocessing && \
    pip install git+https://github.com/keras-team/keras-preprocessing.git && \
    pip install pillow

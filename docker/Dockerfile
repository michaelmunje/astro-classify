ARG BASE_CONTAINER=luke035/nvidia-anaconda-docker
FROM $BASE_CONTAINER

LABEL maintainer="Michael Munje & Danster"

ARG TF

RUN apt-get update && \
    apt-get upgrade -y && \
    conda update -n base conda && \
    pip install --upgrade pip && \
    conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'pytest' \
    'keras' \
    'pytest-cov' \
    'matplotlib' \
    'pillow' \
    'jupyter' \
    'boto3' \
    $TF && \
    pip install 'jupyter-tensorboard' && \
    conda install openjdk && \
    conda clean -tipsy && \
    conda install -c astropy astroquery && \
    mkdir .astropy && \
    chmod 667 .astropy && \
    apt-get install -y git && \
    apt-get install -y libsm6 libxext6 libxrender-dev && \
    pip uninstall -y keras-preprocessing && \
    pip install git+https://github.com/keras-team/keras-preprocessing.git

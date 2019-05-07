FROM tensorflow/tensorflow:1.13.1-gpu-py3

RUN apt-get update && apt-get install -y --no-install-recommends curl wget

RUN pip install --upgrade pip && \
    pip install \
    'numpy' \
    'pandas' \
    'pytest' \
    'keras' \
    'pillow' \
    'boto3' && \
    apt-get install -y git && \
    apt-get install -y libsm6 libxext6 libxrender-dev

COPY . /opt/ml/code

COPY aws/sagemaker/galana-classifier/train /opt/ml/code

ENV PATH="/opt/ml/code:${PATH}"

WORKDIR /opt/ml/code



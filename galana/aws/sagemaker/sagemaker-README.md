# Using sagemaker for training
This directory (will) contain two dockerfiles and instructions for training on AWS Sagemaker. Some setup required, such as uploading your data to s3 and setting up an output bucket. It might be nice to automate the setup with some kind of IoC script eventually.


## aws-classifier
Will contain a dockerfile and setup instructions for training a classifier that uses AWS's classification algorithms.

## galana-classifier
Will contain a dockerfile and setup instructions for training the galana classifier inside galana/models/construct.py. Trained model will be output to s3 for use.

## Making inferences
It's possible to use sagemaker to run inferences as well, by setting up Endpoints. Endpoints can be backed by AWS sagemaker framework code or a custom container with whatever inference code you want. For now assume that you'll need to grab the model manually out of S3 when it's time ot make inferences.

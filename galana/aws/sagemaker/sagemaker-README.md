# Using sagemaker for training
This directory (will) contain two dockerfiles and instructions for training on AWS Sagemaker. Some setup required, such as uploading your data to s3 and setting up an output bucket. It might be nice to automate the setup with some kind of IoC script eventually.

Before beginning, make sure you've installed and set up the [AWS CLI](https://aws.amazon.com/cli/) -- on Mac and Linux you can install by using `pip install awscli`, then configure it for your account using `aws configure`. See the [AWS CLI configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for more information.

## aws-classifier
Will contain a dockerfile and setup instructions for training a classifier that uses AWS's classification algorithms.

## galana-classifier
Run the `build_and_push.sh` script to build and upload the container to AWS ECR. Your container image is required to be in ECR in order to run it via AWS Sagemaker. **Keep in mind that it will use your default AWS region**. This is important, because us-west-1 doesn't have any GPU instance types available - you may wish to switch to us-west-2 or another region.

Run the `start_training_task.sh` script to trigger the AWS Sagemaker training task. Specify the bucket containing kaggle input data using the `--input-data=BUCKET_NAME` parameter. For the `--output-data=BUCKET_NAME` parameter, specify the bucket you wish to use for saving the trained model.

## Making inferences
It's possible to use sagemaker to run inferences as well, by setting up Endpoints. Endpoints can be backed by AWS sagemaker framework code or a custom container with whatever inference code you want. For now assume that you'll need to grab the model manually out of S3 when it's time ot make inferences.


image=$1
role=$2
inputbucket=$3
outputbucket=$4

if [ "$image" == "" ]
then
    echo "Usage: $0 <ECR-image-name> <role-ARN>"
    exit 1
fi

if [ "$role" == "" ]
then
    echo "Usage: $0 <ECR-image-name> <role-ARN>"
    exit 1
fi

# Get the account number associated with the current IAM credentials
account=$(aws sts get-caller-identity --query Account --output text)

if [ $? -ne 0 ]
then
    exit 255
fi
region=$(aws configure get region)
region=${region:-us-west-2}

fullname="${account}-${region}-$(date +%Y%m%d-%h%m%s)"

echo "Job name: ${fullname}"

aws sagemaker create-training-job \
          --training-job-name ${fullname} \
          --algorithm-specification TrainingImage=${image},TrainingInputMode=File \
          --role-arn ${role} \
          --input-data-config '{"ChannelName" : "kaggle", "DataSource" : { "S3DataSource": { "S3DataType": "S3Prefix", "S3Uri": "'${inputbucket}'", "S3DataDistributionType" : "FullyReplicated" } }, "CompressionType" : "None", "RecordWrapperType" : "None"}' \
          --output-data-config S3OutputPath=${outputbucket} \
          --resource-config InstanceType=ml.p2.xlarge,InstanceCount=1,VolumeSizeInGB=50 \
          --stopping-condition MaxRuntimeInSeconds=43200

import boto3


def box_to_tf_record():
    pass


def detect_boxes():
    bucket = 'galana-data-mining'

    s3 = boto3.resource('s3')

    bucket_galana = s3.Bucket(bucket)

    galaxy_files = list()

    for obj in bucket_galana.objects.all():
        if obj.key.startswith('ml/') and obj.key.endswith('.jpg'):
            galaxy_files.append(obj.key)

    client = boto3.client('rekognition')

    for photo in galaxy_files:

        response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                        MaxLabels=10)

        print('Detected labels for ' + photo)
        print()
        for label in response['Labels']:
            for instance in label['Instances']:
                print("  Bounding box")
                print("    Top: " + str(instance['BoundingBox']['Top']))
                print("    Left: " + str(instance['BoundingBox']['Left']))
                print("    Width: " + str(instance['BoundingBox']['Width']))
                print("    Height: " + str(instance['BoundingBox']['Height']))
                print("    Confidence: " + str(instance['Confidence']))
                print()
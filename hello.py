import boto3

client = boto3.client('rekognition')

response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'aws-ml-guide',
            'Name': 'Marvel.jpg',
        },
    },
)

print(response)
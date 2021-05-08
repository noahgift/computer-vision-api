#!/usr/bin/env python3

import click
import boto3

@click.command(help="This tool does label detection")
@click.option('--file', prompt='I need the name of the file in the bucket',
              help='This is the name of the file in the bucket')
def detect(file):
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'aws-ml-guide',
                'Name': file,
            },
        },
    )
    click.echo(click.style(f"Detecting Labels for: {file}", fg="red"))
    labels = response['Labels']
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']
        click.echo(click.style(f"{name}: {confidence}", fg="green"))

if __name__ == '__main__':
    # pylint: disable=E1120
    detect()

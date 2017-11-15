#!/usr/bin/python
import boto3

#Use the credentials stored in ~/.aws/credentials
BUCKET_NAME = 'xxx'
KEY = 'xxx.msi'


s3 = boto3.resource('s3')

#Using the BUCKET_NAME defined above, download the file defined by KEY above
s3.Bucket(BUCKET_NAME).download_file(KEY, 'xxx.msi')


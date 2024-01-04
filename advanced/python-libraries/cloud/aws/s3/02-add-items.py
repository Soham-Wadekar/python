import random
import os
import boto3

s3 = boto3.resource("s3")

buckets = [bucket.name for bucket in s3.buckets.all()]
files = os.listdir("advanced/python-libraries/cloud/aws/s3/test_files")

for file in files:
    bucket_name = random.choice(buckets)
    file_path = "advanced/python-libraries/cloud/aws/s3/test_files/" + file

    s3.Bucket(bucket_name).upload_file(file_path, file)

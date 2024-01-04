import boto3

s3 = boto3.resource("s3")

bucket_name = "test-bucket-sohamw"

for i in range(3):
    s3.create_bucket(
        Bucket=bucket_name + "-" + str(i),
        CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},
    )

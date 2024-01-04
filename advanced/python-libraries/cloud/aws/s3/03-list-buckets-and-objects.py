import boto3

s3 = boto3.resource("s3")

for bucket in s3.buckets.all():
    print(f"Bucket: {bucket.name}")
    print("Objects:")
    for obj in s3.Bucket(bucket.name).objects.all():
        print(f"{obj.key}")
    print()

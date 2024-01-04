import boto3

s3 = boto3.resource("s3")

# Deleting all objects from all buckets (buckets must be empty before deletion)
for bucket in s3.buckets.all():
    for obj in s3.Bucket(bucket.name).objects.all():
        print(f"Deleting...: {obj.key} from {bucket.name}")
        s3.Object(bucket.name, obj.key).delete()
    print()

for bucket in s3.buckets.all():
    print(f"Deleting...: {bucket.name}")
    s3.Bucket(bucket.name).delete()

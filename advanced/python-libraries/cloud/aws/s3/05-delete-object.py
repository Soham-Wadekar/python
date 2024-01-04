import boto3

s3 = boto3.resource("s3")

bucket_name = "test-bucket-sohamw-1"
object_name = "test-img-1.jpg"

print("Before Deletion:")
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)

try:
    s3.Object(bucket_name, object_name).delete()
except Exception as e:
    print("Object not found!")
    print(e)

print("\nAfter Deletion:")
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)

import boto3

s3 = boto3.resource("s3")

# Added a file externally to the bucket
for obj in s3.Bucket("test-bucket-sohamw-0").objects.all():
    print(obj.key)

bucket_name = "test-bucket-sohamw-0"
object_name = "test-img-6.jpg"
download_path = "advanced/python-libraries/cloud/aws/s3/test_files/test-img-6.jpg"

s3.Bucket(bucket_name).download_file(object_name, download_path)

import boto3

ec2 = boto3.resource('ec2')

instance_id = "i-087555537da18b5e4"
instance = ec2.Instance(instance_id)

response = instance.start()
print(f"Starting Instance: {response}")
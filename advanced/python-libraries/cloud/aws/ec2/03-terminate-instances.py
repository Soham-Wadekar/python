import boto3

ec2 = boto3.resource('ec2')

instance_id = 'i-0597d4fccfc72c32b'         # Running instance
instance = ec2.Instance(instance_id)

response = instance.terminate()
print(f"Termination Response: {response}")
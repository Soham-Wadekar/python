import boto3

ec2 = boto3.resource('ec2')

instance_name = 'MyInstance'

instances = ec2.create_instances(
    ImageId = "ami-0a0f1259dd1c90938",
    MinCount = 3,                           # Specify how many instances are needed to be created
    MaxCount = 3,
    InstanceType = "t2.micro",
    KeyName = "testkey",
    SubnetId = "subnet-0020b12cc0b447969",
    TagSpecifications = [
        {
            'ResourceType': "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": instance_name
                }
            ]
        }
    ]
)

for instance in instances:
    print(f"Created instance with ID: {instance}")
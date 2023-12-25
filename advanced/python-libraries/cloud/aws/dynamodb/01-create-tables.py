import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName = "Books",
    KeySchema = [
        {
            "AttributeName": "BookID",
            "KeyType": "HASH"
        }
    ],
    AttributeDefinitions = [
        {
            "AttributeName": "BookID",
            "AttributeType": "N"
        }
    ],
    ProvisionedThroughput = {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5
    }
)
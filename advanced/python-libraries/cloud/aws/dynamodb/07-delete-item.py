import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Books')

table.delete_item(
    Key = {
        "BookID": 1002
    }
)
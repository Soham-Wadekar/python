import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table("Books")

response = table.query(
    KeyConditionExpression = Key('BookID').eq(1002),
)

items = response.get('Items', [])
print(f"Items found: {items}")
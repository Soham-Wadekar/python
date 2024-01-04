import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Books")

response = table.scan(FilterExpression=Attr("CopiesSold").gt(5_000_000))

items = response.get("Items", [])

for item in items:
    print(
        f"BookID: {item['BookID']}\tTitle: {item['Title']}\tAuthor: {item['Author']}\tCopies Sold: {item['CopiesSold']}"
    )

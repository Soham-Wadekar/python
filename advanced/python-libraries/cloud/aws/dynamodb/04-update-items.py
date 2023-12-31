import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Books")

updation_key = 1003
copies_sold_new = 20_000_000

response = table.update_item(
    Key={"BookID": updation_key},
    UpdateExpression="SET CopiesSold = :value",
    ExpressionAttributeValues={":value": copies_sold_new},
    ReturnValues="UPDATED_NEW",  # Optional
)

updated_item = response.get("Attributes", {})
print(f"Updated Value: {updated_item}")

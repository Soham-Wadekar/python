import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Books")

response = table.get_item(Key={"BookID": 1001})

if "Item" in response:
    print("Item Found!!")
    print(response["Item"])
else:
    print("Item not found")

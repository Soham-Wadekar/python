import boto3

dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")

table = dynamodb.Table("Books")

# Adding items to the table

table.put_item(
    Item={
        "BookID": 1001,
        "Title": "Atomic Habits",
        "Author": "James Clear",
        "CopiesSold": 15_000_000,
    }
)

table.put_item(
    Item={
        "BookID": 1002,
        "Title": "Ikigai",
        "Author": "Hector Garcia",
        "CopiesSold": 3_000_000,
    }
)

table.put_item(
    Item={
        "BookID": 1003,
        "Title": "How to Win Friends and Influence People",
        "Author": "Dale Carnegie",
        "CopiesSold": 16_000_000,
    }
)

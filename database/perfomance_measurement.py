import boto3
import time

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

start = time.time()
item = dynamodb.get_item(TableName="Comment",
Key={
    'ProductName': {'S': 'Custom 2-day City Mini GT Double Stroller'}, 'ReviewDate': {'S': '2018-06-08 09:37:33'}})
end = time.time()

count = dynamodb.describe_table(TableName="Comment")
print("item: ", item)
print("ProductName: Custom 2-day City Mini GT Double Stroller")
print("SubcategoryName: 2018-06-08 09:37:33")
print('time to query 1 record: ', end-start)
print('total_records: ', count["Table"]["ItemCount"])

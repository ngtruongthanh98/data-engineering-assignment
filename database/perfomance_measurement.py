import boto3
import time

start = time.time()
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
end = time.time()

item = dynamodb.get_item(TableName="Product", Key={
          'ProductName': {'S': ' Baby Toys - 0 to 1yr'}, 'SubcategoryName': {'S': 'Digital'}})

count = dynamodb.describe_table(TableName="Product")

print("ProductName: Baby Toys - 0 to 1yr")
print("SubcategoryName: Digital")
print('time to query 1 record: ', end-start)
print('total_record: ', count["Table"]["ItemCount"])

import pyodbc
import boto3

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_eng;Trusted_Connection=yes;')
cursor = connection.cursor()

cursor.execute("SELECT * FROM Production.Product")
columns = [column[0] for column in cursor.description]
print(columns)

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
# client.create_table(
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'name',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'value',
#             'AttributeType': 'S'
#         },
#     ],
#     TableName='myTable',
#     KeySchema=[
#         {
#             'AttributeName': 'name',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'value',
#             'KeyType': 'RANGE'
#         },
#     ],
#     ProvisionedThroughput = {
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5,
#       },
# )
response = client.batch_write_item( 
  RequestItems={
    "myTable": [
        {
            "PutRequest": {
                "Item": {
                    "name": { "S": "Hello" },
                    "value": { "S": "World" }
                }
            }
        }
    ]
  }
)

print(response)

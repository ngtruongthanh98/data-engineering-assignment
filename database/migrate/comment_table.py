import pyodbc
import boto3

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_eng;Trusted_Connection=yes;')
cursor = connection.cursor()

cursor.execute("SELECT * FROM data_eng.Production.ProductReview")
columns = [column[0] for column in cursor.description]

items = []
for row in cursor.fetchall():
    item = {
      "PutRequest": {
        "Item": {}
      }
    }
    for i, column in enumerate(columns):
      if row[i] is not None:
        if isinstance(row[i], bool):
          item["PutRequest"]["Item"][column] = {"BOOL": row[i]}
        elif isinstance(row[i], (int, float)):
          item["PutRequest"]["Item"][column] = {"N": f"{row[i]}"}
        else:
          item["PutRequest"]["Item"][column] = {"S": str(row[i])}
    items.append(item)

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

for item in items:
  response = client.batch_write_item( 
    RequestItems={
      "Comment": [item],
    }
  )


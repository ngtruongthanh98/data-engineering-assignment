import pyodbc
import boto3

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_eng;Trusted_Connection=yes;')
cursor = connection.cursor()

cursor.execute("SELECT p.*, ps.name as SubcategoryName, pc.Name as CategoryName FROM data_eng.Production.Product p " \
"LEFT JOIN data_eng.Production.ProductSubcategory ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID " \
"LEFT JOIN data_eng.Production.ProductCategory pc ON ps.ProductCategoryID = pc.ProductCategoryID")
columns = [column[0] for column in cursor.description]
print(columns)

items = []
for row in cursor.fetchall():
    item = {
      "PutRequest": {
        "Item": {}
      }
    }
    for i, column in enumerate(columns):
      if column == 'Name':
        item["PutRequest"]["Item"]["ProductName"] = {"S": str(row[i])}
      elif row[i] is not None:
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
      "Product": [item],
    }
  )


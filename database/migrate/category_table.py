import mysql.connector
import boto3
import pyodbc

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bq"
)

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_eng;Trusted_Connection=yes;')
mssql_cursor = connection.cursor()
mssql_cursor.execute("select ps.Name as SubcategoryName, pc.Name as CategoryName FROM Production.ProductSubcategory ps left join Production.ProductCategory pc on ps.ProductCategoryID = pc.ProductCategoryID")
mssql_columns = [column[0] for column in mssql_cursor.description]
print("🚀 ~ file: category_table.py ~ line 17 ~ mssql_columns", mssql_columns)

items = []

for row in mssql_cursor.fetchall():
    item = {
      "PutRequest": {
        "Item": {}
      }
    }
    # Add custom column here
    item["PutRequest"]["Item"]["CategoryImage"] = {"S": "https://cf.shopee.vn/file/687f3967b7c2fe6a134a2c11894eea4b_tn"}
    item["PutRequest"]["Item"]["SubcategoryImage"] = {"S": "https://cf.shopee.vn/file/3fb459e3449905545701b418e8220334_tn"}
    for i, column in enumerate(mssql_columns):
      if row[i] is not None:
        if isinstance(row[i], bool):
          item["PutRequest"]["Item"][column] = {"BOOL": row[i]}
        elif isinstance(row[i], (int, float)):
          item["PutRequest"]["Item"][column] = {"N": f"{row[i]}"}
        else:
          item["PutRequest"]["Item"][column] = {"S": str(row[i])}
    items.append(item)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bq"
)

mysql_cursor = mydb.cursor()
mysql_cursor.execute("SELECT c.*, sc.* FROM category_sub_categories csc LEFT JOIN categories c ON csc.category_id = c.id LEFT JOIN sub_categories sc ON sc.id = csc.sub_category_id")

mysql_columns = [column[0] for column in mysql_cursor.description]
print("🚀 ~ file: category_table.py ~ line 14 ~ mysql_columns", mysql_columns)

for row in mysql_cursor:
    item = {
      "PutRequest": {
        "Item": {}
      }
    }
    # Add custom column here
    for i, column in enumerate(mysql_columns):
      if column == 'title':
        item["PutRequest"]["Item"]["CategoryName"] = {"S": str(row[i])}
      if column == 'name':
        item["PutRequest"]["Item"]["SubcategoryName"] = {"S": str(row[i])}
      elif row[i] is not None:
        if isinstance(row[i], bool):
          item["PutRequest"]["Item"][column] = {"BOOL": row[i]}
        elif isinstance(row[i], (int, float)):
          item["PutRequest"]["Item"][column] = {"N": f"{(row[i])}"}
        else:
          item["PutRequest"]["Item"][column] = {"S": str((row[i]))}
    items.append(item)


for item in items:
  response = client.batch_write_item( 
    RequestItems={
      "Category": [item],
    }
  )
  print("🚀 ~ file: category_table.py ~ line 47 ~ response", response["ResponseMetadata"]["HTTPStatusCode"], response["UnprocessedItems"])


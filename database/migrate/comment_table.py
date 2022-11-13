import pyodbc
import boto3
import mysql.connector
import random
import traceback
from essential_generators import DocumentGenerator

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_eng;Trusted_Connection=yes;')
mssql_cursor = connection.cursor()

mssql_cursor.execute("SELECT * FROM data_eng.Production.ProductReview")
mssql_columns = [column[0] for column in mssql_cursor.description]

items = []

dynamodb  = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

product_names = dynamodb.scan(TableName="Product",
  ProjectionExpression="ProductName",
)
product_names = [pn["ProductName"]["S"] for pn in product_names["Items"]]

for row in mssql_cursor.fetchall():
    item = {
      "PutRequest": {
        "Item": {}
      }
    }
    item["PutRequest"]["Item"]["ProductName"] = {'S': random.choice(product_names)}
    for i, column in enumerate(mssql_columns):
      if row[i] is not None:
        if column == 'ReviewerName': column = 'name'
        elif column == "EmailAddress": column = "email"
        elif column == "Rating": column = "overall_score"
        elif column == "Comments": column = "comment"
        if isinstance(row[i], bool):
          item["PutRequest"]["Item"][column] = {"BOOL": row[i]}
        elif isinstance(row[i], (int, float)):
          item["PutRequest"]["Item"][column] = {"N": f"{row[i]}"}
        else:
          item["PutRequest"]["Item"][column] = {"S": str(row[i])}
    items.append(item)


'''MYSQL'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bq"
)

mysql_cursor = mydb.cursor()
mysql_cursor.execute("SELECT * FROM bq.testimonials")

mysql_columns = [column[0] for column in mysql_cursor.description]
print("🚀 ~ file: category_table.py ~ line 14 ~ mysql_columns", mysql_columns)

gen = DocumentGenerator()

for row in mysql_cursor.fetchall():
    item = {
      "PutRequest": {
        "Item": {}
      }
    }
    item["PutRequest"]["Item"]["ProductName"] = {'S': random.choice(product_names)}
    for i, column in enumerate(mysql_columns):
      if column != 'email':
        if row[i] is not None:
          if column == 'created': column = 'ReviewDate'
          if isinstance(row[i], bool):
            item["PutRequest"]["Item"][column] = {"BOOL": row[i]}
          elif isinstance(row[i], (int, float)):
            item["PutRequest"]["Item"][column] = {"N": f"{row[i]}"}
          else:
            item["PutRequest"]["Item"][column] = {"S": str(row[i])}
      else: item["PutRequest"]["Item"][column] = {"S": gen.email()}
    items.append(item)

'''BOTO3 DYNAMODB'''

logf = open("logger.log", "w", encoding='utf-8')

for item in items:
  try:
    response = dynamodb.batch_write_item( 
      RequestItems={
        "Comment": [item],
      }
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
      logf.write("WARNING: {0}: {1}\n".format(str(item["PutRequest"]["Item"]), response))
  except BaseException as e:
    logf.write("ERROR: {0}: {1}\n".format(str(item["PutRequest"]["Item"]), str(e)))
    print(traceback.format_exc())

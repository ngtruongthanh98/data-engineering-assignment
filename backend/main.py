from flask import Flask, request
from flask_cors import CORS
import boto3

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})

# hello world route
@app.route('/', methods=['GET'])
def greeting():
  return 'Hello World'

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

product_index = ['ProductName', 'SubcategoryName', 'CategoryName']


@app.route('/products', methods=['GET'])
def get_products():
  query_columns = request.args.to_dict(flat=False)
  columns = [qc for qc in query_columns]
  
  if any([c for c in columns if c in product_index]):
    if query_columns.get('ProductName') is not None:
      return dynamodb.get_item(TableName="Product", Key={
          'ProductName': {'S': query_columns.get('ProductName')[0]}})
    elif query_columns.get('CategoryName') is not None:
        return dynamodb.query(
            TableName="Product", IndexName='CategoryGlobalIndex',
            ExpressionAttributeValues={':categoryName': {
                'S': query_columns.get('CategoryName')[0],
            }},
            KeyConditionExpression='CategoryName = :categoryName'
        )
    elif query_columns.get('SubcategoryName') is not None:
      return dynamodb.query(
          TableName="Product", IndexName='SubcategoryGlobalIndex',
          ExpressionAttributeValues={':subcategoryName': {
              'S': query_columns.get('SubcategoryName')[0],
          }},
          KeyConditionExpression='SubcategoryName = :subcategoryName'
      )
  # else:
  #   def camelCase(s): return s[:1].lower() + s[1:] if s else ''
  #   expression_attribute_values = {}
  #   for column in columns:
  #     expression_attribute_values[':' + camelCase(
  #         column)] = query_columns.get(column)[0]
  #     print("🚀 ~ file: main.py ~ line 56 ~ expression_attribute_values", expression_attribute_values)
  #   return dynamodb.scan(
  #       TableName="Product", FilterExpression="ProductName = :z", ExpressionAttributeValues={':z': {'S':'HL Nipple'}})
  
if __name__ == '__main__':
  app.run(debug=True)

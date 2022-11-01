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


@app.route('/comments', methods=['GET'])
def get_comments():
  max_items = request.args.get('max_items')
  max_items = 5 if max_items is not None else 5
  page_size = request.args.get('page_size')
  page_size = 5 if page_size is not None else 5
  starting_token = request.args.get('starting_token')
  productID = request.args.get('productID')

  if productID is None: return {"status": False, "message": "provide productID"}

  paginator = dynamodb.get_paginator('query')
  result = paginator.paginate(TableName="Comment",
                                       ExpressionAttributeValues={':productID': {
                                           'N': productID,
                                       }}, KeyConditionExpression='ProductID = :productID',
                                       PaginationConfig={
                                           'MaxItems': max_items,
                                           'PageSize': page_size,
                                           'StartingToken': starting_token
                                       }).build_full_result()
  return result

if __name__ == '__main__':
  app.run(debug=True)

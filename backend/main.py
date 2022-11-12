from flask import Flask, request
from flask_cors import CORS
import boto3
import json
from urllib.parse import urlencode

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
      result = dynamodb.get_item(TableName="Product", Key={
          'ProductName': {'S': query_columns.get('ProductName')[0]}})
    elif query_columns.get('CategoryName') is not None:
        result = dynamodb.query(
            TableName="Product", IndexName='CategoryGlobalIndex',
            ExpressionAttributeValues={':categoryName': {
                'S': query_columns.get('CategoryName')[0],
            }},
            KeyConditionExpression='CategoryName = :categoryName'
        )
    elif query_columns.get('SubcategoryName') is not None:
      result = dynamodb.query(
          TableName="Product", IndexName='SubcategoryGlobalIndex',
          ExpressionAttributeValues={':subcategoryName': {
              'S': query_columns.get('SubcategoryName')[0],
          }},
          KeyConditionExpression='SubcategoryName = :subcategoryName'
      )
  return serialize(result)
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

  if productID is None:
    return {"status": False, "message": "provide productID"}

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

@app.route('/categories', methods=['GET'])
def get_categories():
  categories = dynamodb.scan(
    ProjectionExpression="CategoryImage,CategoryName",
    TableName="Product", IndexName='CategoryGlobalIndex')
  result = serialize(categories, True)
  for item in result["data"]:
    item["link"] =  "/subcategories?" + urlencode({'CategoryName': item['categoryName']})
  return result


@app.route('/subcategories', methods=['GET'])
def get_subcategories():
  CategoryName = request.args.get('CategoryName')
  subcategories = dynamodb.scan(
    TableName="Product", IndexName='SubcategoryGlobalIndex', FilterExpression="CategoryName = :z", ExpressionAttributeValues={':z': {'S': CategoryName}}
  )
  result = serialize(subcategories)
  for item in result["data"]:
    item["link"] =  "/products?" + urlencode({'ProductName': item['productName']})

  return result


def serialize(model, unique=False):
  def remove_reports_duplicate(list: list) -> list:
      elm_to_string = [json.dumps(l) for l in list]
      unique_reports = set(elm_to_string)
      return [json.loads(report) for report in unique_reports]
      
  def to_camel_case(str) -> str:
    return str[0].lower() + str[1:]

  def serialize_item(item):
    new_item = {}
    for key, item_data in item.items():
      key = to_camel_case(key)
      for _, item_value in item_data.items():
        new_item[key] = item_value
    return new_item

  dict = {}
  if 'Count' in model:
    for item in model["Items"]:
      new_item = serialize_item(item)
      dict.setdefault('data', []).append(new_item)
      if unique:
        dict["data"] = remove_reports_duplicate(dict["data"])
    dict["total"] = len(dict["data"])
  elif 'Item' in model: 
    dict = serialize_item(model["Item"])
  return dict

  
if __name__ == '__main__':
  app.run(debug=True)

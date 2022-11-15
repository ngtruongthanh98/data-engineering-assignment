from flask import Flask, request
from flask_cors import CORS
import boto3
import json
from urllib.parse import urlencode
from random import randint

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})

# hello world route


@app.route('/', methods=['GET'])
def greeting():
  return 'Hello World'


dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')


@app.route('/products', methods=['GET'])
def get_products():
  query_columns = request.args.to_dict(flat=False)

  if query_columns.get('ProductName') is not None:
    result = dynamodb.query(TableName="Product",
        IndexName='ProductNameGlobalIndex', 
        ExpressionAttributeValues={ 
          ':productName': {'S': query_columns.get('ProductName')[0]}
        },
        KeyConditionExpression='ProductName = :productName')
  elif query_columns.get('SubcategoryName') is not None:
    result = dynamodb.query(
        TableName="Product",
        ExpressionAttributeValues={':subcategoryName': {
            'S': query_columns.get('SubcategoryName')[0],
        }},
        KeyConditionExpression='SubcategoryName = :subcategoryName'
    )
  return serialize(result)

@app.route('/comments', methods=['GET'])
def get_comments():
  max_items = request.args.get('max_items')
  max_items = 5 if max_items is not None else 5
  page_size = request.args.get('page_size')
  page_size = 5 if page_size is not None else 5
  starting_token = request.args.get('starting_token')
  ProductName = request.args.get('productName')

  if ProductName is None:
    return {"status": False, "message": "provide ProductName"}

  paginator = dynamodb.get_paginator('query')
  result = paginator.paginate(TableName="Comment",
                              ExpressionAttributeValues={':ProductName': {
                                  'S': ProductName,
                              }}, KeyConditionExpression='ProductName = :ProductName',
                              PaginationConfig={
                                  'MaxItems': max_items,
                                  'PageSize': page_size,
                                  'StartingToken': starting_token
                              }).build_full_result()
  return serialize(result)


@app.route('/categories', methods=['GET'])
def get_categories():
  categories = dynamodb.scan(
      ProjectionExpression="CategoryName, image",
      TableName="Category")
  result = serialize(categories, True)
  for item in result["data"]:
    item["link"] = "/subcategories?" + \
        urlencode({'CategoryName': item['categoryName']})
  return result


@app.route('/subcategories', methods=['GET'])
def get_subcategories():
  CategoryName = request.args.get('CategoryName')

  subcategories = dynamodb.query(
      # ProjectionExpression="SubcategoryName",
      ExpressionAttributeValues={':categoryName': {
          'S': CategoryName,
      }}, KeyConditionExpression='CategoryName = :categoryName',  TableName="Category")

  result = serialize(subcategories)
  for item in result["data"]:
    item["link"] =  "/products?" + urlencode({'SubcategoryName': item['subcategoryName']})

  return result


@app.route('/product', methods=['POST'])
def create_new_product():
  body = request.json
  new_item = {}
  for key, value in body.items():
    key = key[0].upper() + key[1:]
    if isinstance(value, bool):
      new_item[key] = {"BOOL": value}
    elif isinstance(value, (int, float)):
      new_item[key] = {"N": f"{value}"}
    else:
      new_item[key] = {"S": str(value)}

  new_item["ProductID"] = {'N': f"{randint(0, 100000)}"}
  return dynamodb.put_item(TableName="Product", Item=new_item)

@app.route('/overview/<table>', methods=['GET'])
def get_overview(table):
  table = table[0].upper() + table[1:]
  return dynamodb.describe_table(TableName=table)

def query_in_list(dynamodb_list: list, attribute_to_query: str):
  unique_dynamodb_list = remove_reports_duplicate(dynamodb_list)
  filter_expression = ''
  expression_value = {}
  for i, element in enumerate(unique_dynamodb_list):
    expression_value[f":cond{i}"] = element[attribute_to_query]
    if i != 0:
      filter_expression += ","
    filter_expression += f":cond{i}"
  return filter_expression, expression_value
  
def remove_reports_duplicate(list: list) -> list:
      elm_to_string = [json.dumps(l) for l in list]
      unique_reports = set(elm_to_string)
      return [json.loads(report) for report in unique_reports]

def serialize(model, unique=False):
  
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
    dict["data"] = []
    for item in model["Items"]:
      new_item = serialize_item(item)
      dict.setdefault('data', []).append(new_item)
      if unique:
        dict["data"] = remove_reports_duplicate(dict["data"])
    dict["total"] = len(dict["data"])
  elif 'Item' in model:
    dict = serialize_item(model["Item"])
  if "NextToken" in model:
    dict["nextToken"] = model["NextToken"]
  return dict


if __name__ == '__main__':
  app.run(debug=True)

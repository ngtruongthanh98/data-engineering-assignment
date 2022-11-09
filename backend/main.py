from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import uuid

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


GAMES = [
  {
    'id': uuid.uuid4().hex,
    'title': 'Identity V',
    'genre': ' horror',
    'played': False
  },
  {
    'id': uuid.uuid4().hex,
    'title': 'Bida',
    'genre': ' sports',
    'played': False
  },
  {   
    'id': uuid.uuid4().hex,    
    'title':'Evil Within',
    'genre':'horror',
    'played': False,
  },
  {   
    'id': uuid.uuid4().hex,    
    'title':'The last of us',
    'genre':'survival',
    'played': True,
  },
  {
    'id': uuid.uuid4().hex,    
    'title':'Days gone',
    'genre':'horror/survival',
    'played': False,
  },
  { 
    'id': uuid.uuid4().hex,  
    'title':'Mario',
    'genre':'retro',
    'played': True,
  }
]

# The GET route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
  response_object = {'status': 'success'}
  if request.method == "POST":
    post_data = request.get_json()
    GAMES.append({
      'id' : uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played'),
    })
    response_object['message'] = 'Game Added!'
  else: 
    response_object['games'] = GAMES
  return jsonify(response_object)
  
@app.route('/categories', methods=['GET'])
def get_categories():
  categories = dynamodb.scan(
          TableName="Product", IndexName='CategoryGlobalIndex')
  categories["Items"] = list(set([c["CategoryName"]["S"] for c in categories["Items"]]))
  categories["Count"] = len(categories["Items"])
  return categories


@app.route('/subcategories', methods=['GET'])
def get_subcategories():
  CategoryName = request.args.get('CategoryName')
  print(CategoryName)
  subcategories = dynamodb.scan(
          TableName="Product", IndexName='SubcategoryGlobalIndex', FilterExpression="CategoryName = :z", ExpressionAttributeValues={':z': {'S':CategoryName}}
      )
  subcategories["Items"] = list(set([c["SubcategoryName"]["S"] for c in subcategories["Items"]]))
  subcategories["Count"] = len(subcategories["Items"])
  return subcategories

if __name__ == '__main__':
  app.run(debug=True)

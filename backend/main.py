from flask import Flask, jsonify, request 
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

# hello world route
@app.route('/', methods=['GET'])
def greeting():
  return 'Hello World'

if __name__ == '__main__':
  app.run(debug=True)
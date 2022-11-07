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

if __name__ == '__main__':
  app.run(debug=True)
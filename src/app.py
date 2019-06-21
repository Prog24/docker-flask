from flask import Flask, jsonify, request
from database import get_db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/mongo')
def mongo():
  db = get_db('sample')
  coll = db['samplecollection']
  result = coll.insert({"name":"hoge","bla":"huga"})
  return jsonify({
    "message": "Hello!!"
  })

@app.route('/hoge', methods=['POST'])
def post_json():
  json = request.get_json()
  return jsonify(json)

@app.route('/hello')
def hello():
  return jsonify({
    "message": "Hello!!"
  })

@app.route('/')
def index():
  return jsonify({
    "message": "テスト!!"
  })

if __name__ == '__main__':
  app.run()

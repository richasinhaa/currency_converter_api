from app import app
from flask import request
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/currencies')
def currencies():
	r = requests.get('https://openexchangerates.org/api/currencies.json')
	return r.json()

@app.route('/converter')
def converter():
	args = request.args
	print (args) # For debugging
	base = args['base']
	to = args['to']
	url = 'https://api.exchangeratesapi.io/latest' + '?base=' + base +'&symbols=' + to
	r = requests.get(url, headers={'Content-Type': 'application/json'})
	r.headers['Access-Control-Allow-Origin'] = '*'
	response = r.json()
	json_string = json.dumps(response)
	resp = json.loads(json_string)
	resp['rate'] = resp['rates'][to]
	return resp

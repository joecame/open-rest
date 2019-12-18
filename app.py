from flask import Flask, jsonify
import requests

langs = ['java', 'javascript','typescript','css','html',
'sql','plsql','plpgsql',
'php','python', 'go', 'rust', 'c', 'c++', 'csharp', 'dart', 'hack', 'shell']

app = Flask(__name__)

@app.route('/')
def index():
	r = requests.get('https://api.github.com/users/haikelfazzani/repos?per_page=200')	
	data = {}
	for v in r.json():
		x = v["language"]
		if x:
			idx = langs.index(x.strip().lower())			
			if x in data:				
				data[x] = data[x] + 1
			else:				
				data[x] = 1

	return jsonify(data)

@app.route('/h/<name>')
def another(name):
	return f'hello world {name}'

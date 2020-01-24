from flask import Blueprint,jsonify
import requests

github = Blueprint('github', __name__)

langs = ['java', 'javascript','typescript','css','html',
'sql','plsql','plpgsql',
'php','python', 'go', 'rust', 'c', 'c++', 'csharp', 'dart', 'hack', 'shell']

@github.route('/api/github/<username>')
def index(username):
	r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=200')	
	total = 0
	data = {}
	persLangs = []

	for v in r.json():
		x = v["language"]
		if x:
			total = total + 1
			idx = langs.index(x.strip().lower())			
			if x in data:				
				data[x] = data[x] + 1
			else:				
				data[x] = 1

	for x in data:
		l = {}
		l["lang"] = x
		l["count"] = data[x]
		l["percent"] = int((data[x] * 100) / total)
		persLangs.append(l)
		
	return jsonify(persLangs)
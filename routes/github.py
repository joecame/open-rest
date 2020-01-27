from flask import Blueprint,jsonify
import requests

github = Blueprint('github', __name__)

langs = ['java', 'javascript','typescript','coffeescript','css','html','vue',
'php','python', 'go', 'rust','ruby', 'c', 'c++', 'c#','lua','r',
'objectif-c','dart', 'swift','kotlin','groovy','scala',
'sql','plsql','plpgsql',
'hack', 'shell', 'pascal', 'assembly','visual basic','perl',
'tex','lex', 'makefile','batchfile', 'cmake', 'nginx','powershell', 'dockerfile',
'arduino',
'matlab','viml'
]

@github.route('/active_users', methods=['GET'])
def active_users():
	response = requests.get('http://www.githubstats.com/contributions/tunisia')
	jsonObj = response.json()
	return jsonify(jsonObj)

@github.route('/<username>', methods=['GET'])
def index(username):
	r = requests.get(f'https://api.github.com/users/{username}/repos?per_page=200')	
	total = 0
	data = {}
	persLangs = []

	for v in r.json():
		x = v["language"]
		if x:
			total = total + 1
			# idx = langs.index(x.strip().lower())
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
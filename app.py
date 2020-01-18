from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS,cross_origin

langs = ['java', 'javascript','typescript','css','html',
'sql','plsql','plpgsql',
'php','python', 'go', 'rust', 'c', 'c++', 'csharp', 'dart', 'hack', 'shell']

languages = ['C', 'Cpp', 'Cpp14', 'Java', 'Python', 'Python3', 'Scala', 'Php', 'Perl', 'Csharp']

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# ['C', 'CPP', 'CPP11', 'CPP14', 'CLOJURE', 'CSHARP', 'GO', 'HASKELL', 
# 'JAVA', 'JAVA8', 'JAVASCRIPT', 'JAVASCRIPT_NODE', 'OBJECTIVEC', 'PASCAL', 
# 'PERL', 'PHP', 'PYTHON', 'PYTHON3', 'R', 'RUBY', 'RUST', 'SCALA', 'SWIFT', 'SWIFT_4_1']
@app.route('/api/runcodev2/<lang>/<code>')
@cross_origin()
def run_code(lang,code):
	# 73a1fc29f9a43c67a8bc996777ebb248d9b8b9cd
	data = {
		'client_secret': '69c68a6905f73de654c15c05744a5e93147c1132',
		'async': 0,
		'source': code,
		'lang': lang.upper(),
		'time_limit': 5,
		'memory_limit': 262144,
	}
	r = requests.post(u'https://api.hackerearth.com/v3/code/run/', data=data)
	return r.json()["run_status"]

@app.route('/api/runcode', methods=['POST'])
@cross_origin()
def gfg_compile():	
	user_code = request.json['code']
	lang_choosed = request.json['lang']
	data = {'lang': lang_choosed,'code': user_code,'input': None,'save': False}
	r = requests.post("https://ide.geeksforgeeks.org/main.php", data=data)
	return r.json()

@app.route('/api/github/<username>')
@cross_origin()
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

@app.route('/api/atom/package/<name>')
@cross_origin()
def atom_package_details(name):
	resp = requests.get(f'https://atom.io/packages/search?q={name}')
	soup = BeautifulSoup(resp.content, 'html.parser')
	elemnt = soup.find('div', class_='grid-cell')

	package_author = elemnt.find('a', class_='author').get_text()
	package_gravatar = elemnt.find('img', class_='gravatar')
	
	package_name = elemnt.find('span', class_='css-truncate-target')
	package_desc = elemnt.find('span', class_='card-description').get_text()
	package_downloads = elemnt.find('span', class_='value').get_text()
	package_stars = elemnt.find('div', class_='star-box').get_text().strip()
	package_url = 'https://atom.io'+package_name.findChildren()[0]['href']

	# get package tags
	package_tags_ul = elemnt.find('ul', class_='keywords').findChildren()
	package_tags = []
	for t in package_tags_ul:
		tagname = t.get_text().replace('#', '')
		if tagname not in package_tags:
			package_tags.append(tagname)

	return jsonify({
		'package_author':package_author.strip(),
		'package_gravatar':package_gravatar['src'],
		'package_name':package_name.get_text(),
		'package_desc':package_desc,
		'package_url':package_url,
		'package_stars':package_stars,
		'package_downloads':package_downloads,
		'package_tags':package_tags
	})
